"""Build the bilingual Health and Governing Agent Actions browser exercises."""
import argparse
import csv
import html
import io
import json
import re
from pathlib import Path
from string import Template
from zipfile import ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
INDEX = {
    "en": dict(title="Free browser exercises", lead="Make a decision, see the evidence and take the exercise with you.",
               eval_title="AI Evaluations", eval_copy="Check a refund answer against the written policy.",
               eval_link="Test the refund answer",
               health_title="Statistics for Health Research", health_copy="Check who is missing before comparing two averages.",
               health_link="Investigate missing measurements",
               gov_title="Governing Agent Actions", gov_copy="Check whether an approval covers a new recipient.",
               gov_link="Check the approval"),
    "pt": dict(title="Exercícios gratuitos no navegador", lead="Tome uma decisão, confira as evidências e leve o exercício com você.",
               eval_title="Avaliações de IA", eval_copy="Confira uma resposta sobre reembolso com a política escrita.",
               eval_link="Teste a resposta de reembolso",
               health_title="Estatística para Pesquisa em Saúde", health_copy="Veja quem ficou de fora antes de comparar duas médias.",
               health_link="Investigue as medidas ausentes",
               gov_title="Governando Ações de Agentes", gov_copy="Confira se a autorização vale para um novo destinatário.",
               gov_link="Confira a autorização"),
}

DEMOS = {
    "health": ("applied-health-statistics", "missing-measurements"),
    "governance": ("governed-agent-operations", "agent-approval-record"),
}
LANG = {
    "en": dict(lang="en", suffix="", other_lang="pt-BR", other_file="index.pt.html",
               other_label="PT-BR", dark_mode="Dark mode", controls="Language and appearance",
               skip="Skip to the exercise", submit="Check my decision", result_title="Decision and evidence",
               result_prompt="Choose an option to see the explanation.",
               noscript="Use the worksheet below to do the exercise without JavaScript.",
               limit_label="What this exercise can tell you", next_title="Use what you learned",
               worksheet_label="Download the worksheet (ZIP)", course_label="Explore the course"),
    "pt": dict(lang="pt-BR", suffix=".pt", other_lang="en", other_file="index.html",
               other_label="EN", dark_mode="Tema escuro", controls="Idioma e aparência",
               skip="Pular para o exercício", submit="Conferir minha decisão", result_title="Decisão e evidência",
               result_prompt="Escolha uma opção para ver a explicação.",
               noscript="Use o material abaixo para fazer o exercício sem JavaScript.",
               limit_label="O que este exercício permite concluir", next_title="Use o que você aprendeu",
               worksheet_label="Baixar o exercício (ZIP)", course_label="Conhecer o curso"),
}
COPY = {
    "health": {
        "en": dict(
            category="STATISTICS FOR HEALTH RESEARCH", title="Who is missing from these averages?",
            lead="Two groups have different day-30 averages. Decide what you would report before comparing them.",
            exercise="Review the day-30 averages", setup_title="The first report",
            setup="A fictional study started with 20 participants in each group. The first report shows only averages.",
            question="What would you report first?", choice_a="Only the two averages",
            choice_b="The averages and how many measurements are missing",
            result_a="Start by reporting the missing measurements.",
            reason_a="The two averages use different proportions of participants. Reporting only the averages hides that difference.",
            result_b="Report the numbers behind both averages.",
            reason_b="That lets the reader see which measurements contributed and where more are missing.",
            limit="These data show how much is missing. To interpret the difference between the averages, investigate why measurements are missing.",
            next_copy="Use the worksheet to draft a report with the available and missing counts. The course takes you from the research question to an analysis you can explain.",
        ),
        "pt": dict(
            category="ESTATÍSTICA PARA PESQUISA EM SAÚDE", title="Quem ficou de fora dessas médias?",
            lead="Dois grupos têm médias diferentes no dia 30. Decida o que você relataria antes de compará-las.",
            exercise="Revise as médias do dia 30", setup_title="O primeiro relatório",
            setup="Um estudo fictício começou com 20 participantes em cada grupo. O primeiro relatório mostra só as médias.",
            question="O que você relataria primeiro?", choice_a="Só as duas médias",
            choice_b="As médias e quantas medidas faltam",
            result_a="Comece por relatar as medidas ausentes.",
            reason_a="As duas médias foram calculadas com proporções diferentes de participantes. Mostrar só as médias esconde essa diferença.",
            result_b="Mostre os números por trás das duas médias.",
            reason_b="Assim, o leitor vê quantas medidas entraram no cálculo e em qual grupo faltam mais.",
            limit="Os dados mostram quantas medidas faltam. Antes de interpretar a diferença entre as médias, investigue por que as medidas estão ausentes.",
            next_copy="Use o material para escrever um relato com as contagens disponíveis e ausentes. No curso, você parte da pergunta de pesquisa e chega a uma análise que consegue explicar.",
        ),
    },
    "governance": {
        "en": dict(
            category="GOVERNING AGENT ACTIONS", title="Does the approval still apply?",
            lead="Your team approved one recipient for an agent’s action. Change the recipient and check what happens to the approval.",
            exercise="Review an agent’s approval", setup_title="What the team approved",
            setup="A fictional team approved sending a project summary to the internal project group.",
            question="Choose a recipient. Does the approval still apply?", choice_a="The same internal group",
            choice_b="An external partner",
            result_a="The internal recipient matches the approval.",
            reason_a="The recipient in this case is the one the team approved. The record can proceed to the remaining checks.",
            result_b="Pause and ask for new approval.",
            reason_b="The partner is outside the approved audience. Record the change and get approval for the new recipient before sending anything.",
            limit="This exercise checks the recipient only. Before taking a real action, the system also needs to check the content, permissions and current rules.",
            next_copy="Use the worksheet to record what was approved, what changed and what should happen next. The course develops that record across several agent actions.",
        ),
        "pt": dict(
            category="GOVERNANDO AÇÕES DE AGENTES", title="A autorização ainda vale?",
            lead="A equipe autorizou um destinatário para a ação de um agente. Troque o destinatário e veja o que acontece com a autorização.",
            exercise="Confira a autorização de um agente", setup_title="O que a equipe autorizou",
            setup="Uma equipe fictícia autorizou o envio de um resumo do projeto para o grupo interno.",
            question="Escolha um destinatário. A autorização ainda vale?", choice_a="O mesmo grupo interno",
            choice_b="Um parceiro externo",
            result_a="O destinatário interno corresponde à autorização.",
            reason_a="O destinatário deste caso é o que a equipe aprovou. O registro pode seguir para as demais checagens.",
            result_b="Suspenda e peça nova autorização.",
            reason_b="O parceiro está fora do público aprovado. Registre a mudança e peça autorização para o novo destinatário antes de enviar.",
            limit="O exercício verifica só o destinatário. Para uma ação real, também é preciso conferir o conteúdo, as permissões e as regras vigentes.",
            next_copy="Use o material para registrar o que foi autorizado, o que mudou e o que deve acontecer em seguida. O curso desenvolve esse registro para diferentes ações de agentes.",
        ),
    },
}


def definitions(entries):
    rows = [
        f"<div><dt>{html.escape(label)}</dt><dd>{html.escape(value)}</dd></div>"
        for label, value in entries
    ]
    return '<dl class="study-summary">' + "".join(rows) + "</dl>"


def health_data(locale, rows):
    example, evidence = [], []
    for row in rows:
        label = f"{'Grupo' if locale == 'pt' else 'Group'} {row['group']}"
        total = int(row["participants"])
        observed = int(row["observed_day_30"])
        missing = total - observed
        rate = f"{missing / total:.0%}"
        example.append((label, row["mean_observed_day_30"]))
        result = f"{missing}/{total} missing ({rate})"
        if locale == "pt":
            result = f"{missing}/{total} ausentes ({rate})"
        evidence.append((label, result))
    return definitions(example), definitions(evidence)


def governance_data(locale):
    if locale == "pt":
        return "", definitions([("Ação", "Enviar um resumo"), ("Autorização registrada", "Grupo interno")])
    return "", definitions([("Action", "Send a summary"), ("Recorded approval", "Internal group")])


def worksheet_zip(worksheet):
    archive = io.BytesIO()
    with ZipFile(archive, "w") as package:
        for suffix in ("", ".pt"):
            name = f"{worksheet}{suffix}.md"
            text = (ROOT / "samples" / name).read_text(encoding="utf-8")
            # Remove the link to the full library. The paired translation stays in the ZIP.
            portable = re.sub(r"(?m)^\[[^\n\]]+\]\(README(?:\.pt)?\.md#[^\n)]+\) · ", "", text)
            package.writestr(ZipInfo(name), portable.encode("utf-8"))
        if worksheet == "missing-measurements":
            csv_name = "data/missing-measurements.csv"
            package.writestr(ZipInfo(csv_name), (ROOT / "samples" / csv_name).read_bytes())
        package.writestr(ZipInfo("LICENSE"), (ROOT / "LICENSE").read_bytes())
    return archive.getvalue()


def render_indexes():
    template = Template((ROOT / "tools" / "demo-index-template.html").read_text(encoding="utf-8"))
    for locale, common in LANG.items():
        base = "../" if locale == "pt" else ""
        alternate = "../demos.html" if locale == "pt" else "pt/demos.html"
        values = {**common, **INDEX[locale], "base": base, "alternate": alternate}
        text = template.substitute({key: html.escape(value) for key, value in values.items()})
        folder = ROOT / "docs" / "pt" if locale == "pt" else ROOT / "docs"
        yield folder / "demos.html", text.encode("utf-8")


def render_files():
    yield from render_indexes()
    template = Template((ROOT / "tools" / "practice-template.html").read_text(encoding="utf-8"))
    links = json.loads((ROOT / "catalog" / "links.json").read_text(encoding="utf-8"))
    with (ROOT / "samples" / "data" / "missing-measurements.csv").open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))
    for demo, (sku, worksheet) in DEMOS.items():
        yield ROOT / "docs" / "downloads" / f"{worksheet}.zip", worksheet_zip(worksheet)
        for locale, common in LANG.items():
            suffix = common["suffix"]
            data, evidence = health_data(locale, rows) if demo == "health" else governance_data(locale)
            plain = {**common, **COPY[demo][locale], "course_url": links[sku][locale],
                     "worksheet_url": f"../downloads/{worksheet}.zip",
                     "demo_index": "../pt/demos.html" if locale == "pt" else "../demos.html"}
            values = {key: html.escape(value) for key, value in plain.items()}
            values.update(example_data=f"        {data}" if data else "", evidence=evidence)
            yield ROOT / "docs" / demo / f"index{suffix}.html", template.substitute(values).encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, output in render_files():
        if args.check:
            if not path.is_file() or path.read_bytes() != output:
                parser.exit(1, f"Regenerate {path.relative_to(ROOT)}.\n")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(output)


if __name__ == "__main__":
    main()
