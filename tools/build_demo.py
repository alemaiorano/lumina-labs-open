"""Regenerate the bilingual static demo from the lab's bundled cases."""
import argparse
import html
import json
import sys
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "labs" / "assertion-gate"
sys.path.insert(0, str(LAB))
from assertion_gate import evaluate

COPY = {
    "en": {
        "html_lang": "en", "other_lang": "pt-BR", "other_url": "pt/index.html",
        "asset_path": "assets", "other_label": "PT-BR", "dark_mode": "Dark mode",
        "skip": "Skip to the lab", "controls": "Language and appearance",
        "category": "LLM EVALUATIONS",
        "title": "Would you ship this answer?",
        "lead": "Test a refund answer against a policy. Change the deadline and see what makes the release gate hold.",
        "experiment": "Refund answer experiment", "policy_title": "Refund policy",
        "policy": "Refunds are processed within 5 business days after approval.",
        "choose": "Which deadline does the answer claim?",
        "option_14": "14 business days", "option_5": "5 business days",
        "run": "Run the gate", "result_title": "Release decision",
        "noscript": "Enable JavaScript for the demo, or run the offline lab below.",
        "result_prompt": "Choose a deadline and test the answer to see the result.",
        "course_next": "Learn to write a test that requires the condition “after approval.”",
        "limit_label": "What this check can miss",
        "limit": "This example uses a fictional policy. The evaluator checks for matching words. It can miss negations and omitted conditions.",
        "local_title": "Run it on your machine",
        "local_copy": "From the repository root, run the full two-case suite. It uses Python’s standard library and needs no API key.",
        "command": "python3 labs/assertion-gate/assertion_gate.py",
        "course_url": "https://lumytics.com/courses/offers/eval-complete/",
        "course_cta": "Explore the LLM evaluation course",
        "footer": "A hands-on sample from Full Harness",
    },
    "pt": {
        "html_lang": "pt-BR", "other_lang": "en", "other_url": "../index.html",
        "asset_path": "../assets", "other_label": "EN", "dark_mode": "Tema escuro",
        "skip": "Pular para o lab", "controls": "Idioma e aparência",
        "category": "AVALIAÇÕES DE LLM",
        "title": "Você liberaria esta resposta?",
        "lead": "Compare uma resposta sobre reembolso com a política. Mude o prazo e veja quando a checagem bloqueia a liberação.",
        "experiment": "Teste da resposta sobre reembolso", "policy_title": "Política de reembolso",
        "policy": "Os reembolsos são processados em até 5 dias úteis após a aprovação.",
        "choose": "Que prazo a resposta afirma?",
        "option_14": "14 dias úteis", "option_5": "5 dias úteis",
        "run": "Testar a resposta", "result_title": "Decisão de liberação",
        "noscript": "Ative o JavaScript para usar a demo ou rode o lab offline abaixo.",
        "result_prompt": "Escolha um prazo e teste a resposta para ver a decisão.",
        "course_next": "Aprenda a escrever um teste que exija a condição “após a aprovação”.",
        "limit_label": "O que a checagem pode deixar passar",
        "limit": "A política é fictícia. O avaliador procura palavras da resposta na política. Pode deixar passar negações ou condições omitidas.",
        "local_title": "Rode na sua máquina",
        "local_copy": "Na raiz do repositório, rode os dois casos completos. Basta a biblioteca padrão do Python. O lab funciona sem chave de API.",
        "command": "python3 labs/assertion-gate/assertion_gate.py --lang pt",
        "course_url": "https://lumytics.com/courses/offers/eval-complete/pt/",
        "course_cta": "Conhecer o curso de avaliação de LLMs",
        "footer": "Uma amostra prática da coleção Full Harness",
    },
}

CASE = {
    "5": {
        "en": "The policy supports the 5-day deadline. The answer meets this case’s threshold.",
        "pt": "A política sustenta o prazo de 5 dias. A resposta atinge o limite deste caso.",
    },
    "14": {
        "en": "The answer introduces 14. The policy only supports 5 business days, so this case blocks release.",
        "pt": "A resposta introduz o número 14. A política só sustenta o prazo de 5 dias úteis, por isso o caso bloqueia a liberação.",
    },
}


def render_files():
    template = Template((ROOT / "tools" / "demo-template.html").read_text(encoding="utf-8"))
    for locale, copy in COPY.items():
        folder = ROOT / "docs" if locale == "en" else ROOT / "docs" / "pt"
        yield folder / "index.html", template.substitute(
            {key: html.escape(value) for key, value in copy.items()}
        )

    rows = [
        json.loads(line)
        for line in (LAB / "samples" / "claims.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    records = {row["id"]: row for row in rows}
    scenarios = {}
    for days, explanation in CASE.items():
        # Vary only the deadline. The graded answer, policy and threshold
        # otherwise come from the same case as in the command-line exercise.
        record = records["refund-14d"]
        verdict = evaluate({**record, "claim": record["claim"].replace("14", days)})
        scenarios[days] = {
            "decision": "PROMOTE" if verdict.passed else "HOLD",
            "score": verdict.score,
            "threshold": verdict.threshold,
            "explanation": explanation,
        }
    yield ROOT / "docs" / "assets" / "scenarios.js", (
        "// Generated by tools/build_demo.py.\nwindow.luminaScenarios = "
        + json.dumps(scenarios, ensure_ascii=False, indent=2)
        + ";\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    stale = []
    for path, content in render_files():
        if not args.check:
            path.write_text(content, encoding="utf-8")
        elif not path.exists() or path.read_text(encoding="utf-8") != content:
            stale.append(str(path.relative_to(ROOT)))
    if stale:
        parser.exit(1, "Regenerate stale demo files: " + ", ".join(stale) + "\n")


if __name__ == "__main__":
    main()
