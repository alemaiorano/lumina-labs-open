"""assertion-gate — turn claim + source + threshold into an executable gate.

The bundled MockLLM is a deterministic lexical groundedness judge. Replace the
single HOOK with a real judge; keep the Verdict contract and fail-closed gate.
Scores, thresholds, and records are illustrative synthetic teaching data.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in",
    "is", "of", "on", "or", "the", "to", "within",
}


@dataclass
class Verdict:
    passed: bool
    evidence: str
    confidence: float
    score: float
    threshold: float


def tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower())
        if token not in STOPWORDS
    }


class MockLLM:
    """Deterministic stand-in for a groundedness judge."""

    def score(self, claim: str, source: str, rubric: str) -> tuple[float, str]:
        claim_tokens = tokens(claim)
        source_tokens = tokens(source)
        if not claim_tokens:
            return 0.0, "claim has no scorable tokens"
        supported = sorted(claim_tokens & source_tokens)
        missing = sorted(claim_tokens - source_tokens)
        score = len(supported) / len(claim_tokens)
        evidence = (
            f"rubric={rubric}; supported={','.join(supported) or '<none>'}; "
            f"missing={','.join(missing) or '<none>'}"
        )
        return score, evidence


# ---- HOOK: replace this instance with a real LLM judge; keep the contract ----
LLM = MockLLM()


def evaluate(record: object) -> Verdict:
    if not isinstance(record, dict):
        return Verdict(False, "record must be a JSON object", 1.0, 0.0, 1.0)
    raw_threshold = record.get("threshold")
    if (
        isinstance(raw_threshold, bool)
        or not isinstance(raw_threshold, (int, float))
        or not 0 <= raw_threshold <= 1
    ):
        return Verdict(False, "threshold must be a number between 0 and 1", 1.0, 0.0, 1.0)

    threshold = float(raw_threshold)
    for field in ("claim", "source"):
        value = record.get(field)
        if not isinstance(value, str) or not tokens(value):
            return Verdict(False, f"{field} must contain words to check", 1.0, 0.0, threshold)
    if record.get("rubric") != "groundedness":
        return Verdict(False, "the only supported rubric is groundedness", 1.0, 0.0, threshold)
    score, evidence = LLM.score(record["claim"], record["source"], record["rubric"])
    return Verdict(
        passed=score > 0 and score >= threshold,
        evidence=evidence,
        confidence=1.0,
        score=score,
        threshold=threshold,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert claim + source + threshold records into executable assertions."
    )
    parser.add_argument(
        "--input",
        default=str(Path(__file__).parent / "samples" / "claims.jsonl"),
        help="jsonl records with id, claim, source, rubric, threshold",
    )
    parser.add_argument("--lang", choices=("en", "pt"), default="en")
    parser.add_argument(
        "--ci", action="store_true",
        help="return exit 1 when any assertion fails (default teaching run always exits 0)",
    )
    args = parser.parse_args()

    try:
        rows = Path(args.input).read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError):
        parser.error("input must be a readable UTF-8 file")
    labels = {
        "en": {
            "header": "id       score   bar  verdict  evidence",
            "gate": "release gate",
            "contract": "claim + source + rubric + threshold = an assertion that can fail",
        },
        "pt": {
            "header": "id       nota limite  decisão evidência",
            "gate": "checagem de liberação",
            "contract": "afirmação + fonte + rubrica + limite = uma asserção que pode falhar",
        },
    }[args.lang]
    print(labels["header"])
    print("-" * 78)
    verdicts = []
    for index, row in enumerate(rows, start=1):
        if not row.strip():
            continue
        record_id = f"row-{index}"
        try:
            record = json.loads(row)
        except json.JSONDecodeError:
            verdict = Verdict(False, "invalid JSON on this line", 1.0, 0.0, 1.0)
        else:
            if isinstance(record, dict):
                record_id = str(record.get("id", record_id))
            verdict = evaluate(record)
        verdicts.append(verdict)
        status = "PASS" if verdict.passed else "FAIL"
        evidence = verdict.evidence
        if args.lang == "pt":
            evidence = (
                evidence.replace("rubric=groundedness;", "rubrica=apoio na fonte;")
                .replace("supported=", "na_fonte=")
                .replace("missing=", "ausentes=")
                .replace("<none>", "<nenhum>")
                .replace("threshold must be a number between 0 and 1", "o limite deve ser um número entre 0 e 1")
                .replace("record must be a JSON object", "cada registro deve ser um objeto JSON")
                .replace("invalid JSON on this line", "JSON inválido nesta linha")
                .replace("claim must contain words to check", "a afirmação deve conter palavras para verificar")
                .replace("source must contain words to check", "a fonte deve conter palavras para verificar")
                .replace("the only supported rubric is groundedness", "o único critério implementado é apoio na fonte")
            )
        print(
            f"{record_id:<8} {verdict.score:>5.2f}  {verdict.threshold:>4.2f}  "
            f"{status:<7}  {evidence}"
        )

    passed = sum(verdict.passed for verdict in verdicts)
    gate_passed = bool(verdicts) and passed == len(verdicts)
    decision = "PROMOTE" if gate_passed else "HOLD"
    summary = "assertions passed" if args.lang == "en" else "asserções passaram"
    print(f"\n{labels['gate']}: {passed}/{len(verdicts)} {summary} -> {decision}")
    print(labels["contract"])
    if args.ci and not gate_passed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
