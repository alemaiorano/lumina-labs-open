# Como testar uma resposta sobre reembolso

[Voltar aos exercícios](README.pt.md#eval-complete) · [Read in English](refund-test-case.md)

**Política fictícia.** Os reembolsos são processados em até 5 dias úteis após a aprovação.

**Resposta da IA.** “Os reembolsos são processados em até 14 dias úteis.”

Reescreva a resposta e use o modelo abaixo para decidir quais versões uma checagem deve aceitar. Você pode preencher o modelo no papel ou copiar para o arquivo de testes da sua equipe.

| Campo | Seu caso de teste |
| --- | --- |
| Pergunta feita à IA | |
| Trecho da política que sustenta a resposta | |
| Número e unidade que a resposta precisa preservar | |
| Condição que a resposta precisa mencionar | |
| Exemplo de resposta que deve passar | |
| Exemplo de resposta que deve falhar | |

<details>
<summary>Compare com a resposta comentada</summary>

A resposta **“O reembolso é processado em até 5 dias úteis após a aprovação”** preserva o prazo e o momento em que ele começa. Teste também duas falhas separadas: **14 dias úteis após a aprovação** e **5 dias úteis** sem dizer que o prazo só começa após a aprovação. Assim, uma versão que corrige o número, mas continua omitindo a condição, ainda falha no seu teste.

</details>

Se quiser executar o exemplo e comparar os resultados, use os [casos em JSONL](../labs/assertion-gate/samples/claims.jsonl) e as [instruções do lab](../labs/assertion-gate/README.pt.md). O código fornecido confere palavras. A condição acima é uma verificação que você pode acrescentar ao seu próprio teste.

**O que aprender em seguida.** Escreva uma checagem para a condição “após a aprovação” e use o mesmo caso para detectar se o erro volta em outra versão. [Conheça o curso de Avaliações de IA](https://lumytics.com/courses/offers/eval-complete/pt/).
