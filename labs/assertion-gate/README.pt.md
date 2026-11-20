# Um prazo sem respaldo bloqueia a liberação

Compare duas respostas sobre reembolso com a mesma política. Corrija o número sem respaldo e confira a nova decisão.

## Como rodar

```sh
python3 assertion_gate.py --lang pt
```

A execução padrão encerra com código 0 para você inspecionar a saída. Use `--ci` quando uma falha deva retornar código 1.

A entrada usa um objeto JSON por linha. Use afirmação e fonte com palavras para verificar, o critério `groundedness` e um limite numérico de 0 a 1. Uma resposta sem palavras em comum com a fonte sempre falha.

## Saída esperada

```text
id       nota limite  decisão evidência
------------------------------------------------------------------------------
refund-5d  1.00  0.80  PASS     rubrica=apoio na fonte; na_fonte=5,business,days,processed,refunds; ausentes=<nenhum>
refund-14d  0.80  0.90  FAIL     rubrica=apoio na fonte; na_fonte=business,days,processed,refunds; ausentes=14

checagem de liberação: 1/2 asserções passaram -> HOLD
afirmação + fonte + rubrica + limite = uma asserção que pode falhar
```

## O que mudar

Troque só o número `14` por `5` na afirmação que falhou. O notebook faz isso em uma cópia temporária. Rode a checagem novamente e explique o que mudou na evidência.

[Notebook](assertion-gate.pt.ipynb)

## Como interpretar

A nota mede a presença de palavras na fonte usada neste exemplo. O teste pode deixar passar uma negação ou a condição **após a aprovação**. Os números e as notas são sintéticos.

[MIT](../../LICENSE)
