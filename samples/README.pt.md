# Casos práticos do Lumina Labs

[Ver todas as ofertas](../README.pt.md) · [Read in English](README.md)

Cada caso traz uma decisão trabalhada em uma das ofertas. Leia a situação fictícia, escreva a sua decisão em uma frase e compare com a resposta comentada.

## Comece pelo método

<a name="core"></a>

### Método Harness Dirigido por Juízes

Uma nova versão do assistente de suporte passa em 19 de 20 checagens. A única falha informa um prazo de reembolso incorreto, e acertar o prazo é um requisito.

**Você libera pela taxa geral de aprovação ou bloqueia por causa do requisito?**

<details>
<summary>Ver resposta comentada</summary>

Bloqueie. Uma checagem obrigatória falhou. Registre a afirmação, a política que ela contradiz e o que precisa passar na próxima execução.

</details>

**O que aprender em seguida.** Aprenda a transformar uma falha observada em uma checagem e registrar quando ela deve impedir o lançamento.

[Ver curso](https://lumytics.com/courses/offers/core/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=67fdsxcb)

<a name="full-harness"></a>

### O Harness Completo

A nova versão acerta 97 de 100 respostas. A anterior acertava 98, e o mínimo é 95. O custo cai de 4 para 3 unidades por solicitação e fica dentro do orçamento. Uma checagem obrigatória mostra que um perfil sem autorização consegue ler um registro privado.

**O que você libera agora e de quais evidências precisaria para reconsiderar?**

[Preencha o registro de decisão](full-harness-decision.pt.md)

<details>
<summary>Ver resposta comentada</summary>

Bloqueie a candidata e mantenha a versão atual. Registre a queda nos acertos e a economia. Defina quem corrige o acesso e repita as checagens de acesso, qualidade e custo com a versão corrigida antes de reconsiderar.

</details>

**O que aprender em seguida.** Pratique a mesma decisão com evidências de outras áreas, como qualidade dos dados, segurança e custo.

[Ver curso](https://lumytics.com/courses/vitrine/pt/#offer-full-harness) · [Comprar na Hotmart](https://pay.hotmart.com/?off=47sschle)

## Aplique o método à sua área

<a name="eval-complete"></a>

### Lançar Aplicações com LLM e Evidências

Um assistente de suporte informa a data errada. O texto recuperado contém a data correta, e a avaliação aponta a divergência.

**Você ajustaria a busca primeiro ou verificaria como a resposta usou o trecho recuperado?**

[Use o modelo de teste de reembolso](refund-test-case.pt.md)

<details>
<summary>Ver resposta comentada</summary>

Inspecione a resposta e sua evidência primeiro. A busca trouxe a data correta neste caso. Adicione um teste de regressão que avalie a resposta junto com o trecho que deveria sustentá-la.

</details>

**O que aprender em seguida.** Aprenda a escrever um teste que exija a condição “após a aprovação” e a verificar se a falha volta em outra versão.

[Ver curso](https://lumytics.com/courses/offers/eval-complete/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=zlmpjbkt)

<a name="coding-complete"></a>

### Harness de Codificação Agêntica

Um agente corrige o arredondamento de faturas e os testes unitários passam. Ele também muda como o sistema mantém usuários conectados, algo que a equipe não autorizou.

**Você aprova as mudanças ou pede que o agente mantenha apenas a correção das faturas?**

<details>
<summary>Ver resposta comentada</summary>

Peça só a correção das faturas. Os testes mostram o que foi verificado. A alteração nas sessões precisa de objetivo e testes próprios.

</details>

**O que aprender em seguida.** Defina limites para uma tarefa de código antes de entregá-la ao agente e use os testes para justificar sua revisão.

[Ver curso](https://lumytics.com/courses/offers/coding-complete/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=lhebjuwa)

<a name="security-complete"></a>

### Segurança de Aplicações com LLM

Um assistente resume documentos de uma pasta aprovada, com acesso de leitura. A pessoa responsável pelo produto propõe dar também permissão de escrita por conveniência.

**Qual permissão o assistente deve ter e o que você verificaria antes de liberar?**

<details>
<summary>Ver resposta comentada</summary>

Mantenha o acesso de leitura. Teste se o assistente consegue ler os documentos autorizados e se o sistema impede gravações. Registre onde e como fez a checagem.

</details>

**O que aprender em seguida.** Documente o que o assistente pode acessar e transforme essas permissões em checagens defensivas que a equipe possa repetir.

[Ver curso](https://lumytics.com/courses/offers/security-complete/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=6c6sishb)

<a name="dogfooding-complete"></a>

### Dogfooding

Uma pessoa da equipe diz que o seletor de idioma às vezes volta para a página inicial. O registro do navegador mostra que ela estava numa oferta de curso em português.

**O que entra num teste que outra pessoa consiga repetir?**

<details>
<summary>Ver resposta comentada</summary>

Comece pela oferta em português. Troque para inglês e verifique se a oferta correspondente abriu. Registre a rota inicial, a ação, o destino esperado e o resultado observado.

</details>

**O que aprender em seguida.** Transforme um relato de uso em um teste que detecte se o mesmo problema volta depois de uma mudança.

[Ver curso](https://lumytics.com/courses/offers/dogfooding-complete/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=dde04o38)

<a name="synthetic-complete"></a>

### Usuários Sintéticos e Personas

Três alunos simulados não encontram o link para baixar um arquivo. Todos os perfis simulados descrevem pessoas que usam notebook e já conhecem o GitHub.

**O que dá para concluir e o que você testaria em seguida?**

<details>
<summary>Ver resposta comentada</summary>

Trate a dificuldade de encontrar o link como hipótese. Observe pessoas reais tentando encontrá-lo no celular e no notebook. Registre se conseguem sem ajuda e onde hesitam.

</details>

**O que aprender em seguida.** Varie os perfis simulados e use as diferenças para definir o que observar em testes com pessoas reais.

[Ver curso](https://lumytics.com/courses/offers/synthetic-complete/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=r6kkpeh1)

<a name="data-complete"></a>

### Flywheel de Dados

O mesmo relato de falha entra duas vezes no conjunto de dados. Uma cópia vai para os exemplos usados no ajuste e outra para o conjunto de teste reservado.

**Como corrigir a divisão antes de divulgar um resultado?**

<details>
<summary>Ver resposta comentada</summary>

Agrupe exemplos iguais ou muito parecidos antes de separar os dados. Mantenha cada grupo inteiro em um dos conjuntos. Repita a avaliação com o conjunto de teste corrigido.

</details>

**O que aprender em seguida.** Decida quais exemplos entram no ajuste e quais devem ficar reservados para uma avaliação independente.

[Ver curso](https://lumytics.com/courses/offers/data-complete/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=g278kkug)

<a name="cost-complete"></a>

### Harness de Custo e Latência

O modelo A custa 4 unidades por solicitação e responde em até 1,1 segundo em 95% das solicitações medidas. O B custa 2 unidades e responde em até 1,8 segundo em 95%. Ambos atendem ao requisito de qualidade. A meta é atingir 95% em até 1,5 segundo. O orçamento é de até 4 unidades por solicitação.

**Qual configuração atende às condições e o que faria você reconsiderar?**

<details>
<summary>Ver resposta comentada</summary>

Só A atende ao orçamento, ao tempo e à qualidade. Reavalie B se ele atingir o tempo exigido com um volume de solicitações parecido com o esperado e continuar dentro do orçamento e do requisito de qualidade.

</details>

**O que aprender em seguida.** Compare novas configurações com os mesmos requisitos de custo, tempo de resposta e qualidade.

[Ver curso](https://lumytics.com/courses/offers/cost-complete/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=nff1fqnh)

## Cursos independentes

<a name="applied-health-statistics"></a>

### Estatística Aplicada à Pesquisa em Saúde

Num estudo fictício, há medidas do dia 30 para 18 de 20 participantes num grupo e 12 de 20 no outro. O relatório só apresenta as médias observadas.

**O que você acrescentaria antes de comparar as médias?**

[Relate as medidas ausentes](missing-measurements.pt.md)

<details>
<summary>Ver resposta comentada</summary>

Informe quantas medidas foram observadas e quantas faltam em cada grupo, o total de participantes e como tratou as medidas ausentes. Explique como a diferença na quantidade de medidas ausentes pode afetar a interpretação.

</details>

**O que aprender em seguida.** Planeje a análise antes de ver os resultados e registre como medidas ausentes afetam o que você pode concluir.

[Ver curso](https://lumytics.com/courses/applied-health-statistics/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=upe6rst6)

<a name="ai-product-development-harness"></a>

### Harness de Desenvolvimento de Produtos com IA

Um protótipo encaminha solicitações. Uma categoria não tem equipe responsável. Hoje, o protótipo envia essa categoria para a primeira equipe da lista.

**Qual comportamento e qual evidência você exigiria antes da entrega?**

<details>
<summary>Ver resposta comentada</summary>

Defina quem deve conferir as solicitações sem equipe responsável. Teste uma solicitação com destino definido e outra que exija revisão. Registre onde encontrar o resultado de cada teste.

</details>

**O que aprender em seguida.** Especifique como o produto deve se comportar quando falta uma informação e prepare testes que outra pessoa possa conferir.

[Ver curso](https://lumytics.com/courses/ai-product-development-harness/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=cyzdf12o)

<a name="governed-agent-operations"></a>

### Governando Ações de Agentes

A equipe aprova o envio de um resumo para um grupo interno. Antes de executar, o destinatário muda para um endereço externo.

**O agente pode reaproveitar a autorização original?**

[Preencha o registro de autorização](agent-approval-record.pt.md)

<details>
<summary>Ver resposta comentada</summary>

Suspenda a ação. O público mudou. Vincule a autorização ao destinatário e ao escopo reais, registre a mudança e peça nova confirmação antes de executar.

</details>

**O que aprender em seguida.** Registre quem autorizou uma ação, quais limites foram aprovados e quando o agente precisa pedir confirmação de novo.

[Ver curso](https://lumytics.com/courses/governed-agent-operations/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=8bvx22b1)

<a name="experience-quality-harness"></a>

### Harness de Qualidade da Experiência

O formulário de pagamento parece correto na captura de tela. Ao fechar pelo teclado a janela de endereço, a seleção volta para o topo da página.

**Que evidência permitiria que outra pessoa reproduzisse o problema?**

<details>
<summary>Ver resposta comentada</summary>

Anote as teclas usadas, o controle selecionado no início e onde a seleção aparece ao fechar. Confira se ela volta ao controle que abriu a janela. Use a captura como contexto.

</details>

**O que aprender em seguida.** Junte registros de teclado, tela e estrutura para que outra pessoa possa reproduzir o problema e verificar a correção.

[Ver curso](https://lumytics.com/courses/experience-quality-harness/pt/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=5rpgdin8)

## Pacote para agentes de código

<a name="ai-coding-os"></a>

### AI Coding OS · 18 skills para agentes de código

Um agente de código entrega uma revisão dizendo apenas que está tudo certo. A equipe precisa de algo que outra pessoa consiga conferir.

**Qual formato de saída você pediria para esse fluxo de revisão?**

<details>
<summary>Ver resposta comentada</summary>

Peça o escopo, achados concretos com referências a arquivos, verificações que de fato rodaram e incertezas restantes. Outra pessoa poderá conferir cada afirmação pela evidência.

</details>

**O que aprender em seguida.** Adapte instruções de revisão em Markdown para pedir evidências que outra pessoa consiga conferir.

[Ver detalhes do pacote](https://lumytics.com/recursos/ai-coding-os/) · [Comprar na Hotmart](https://pay.hotmart.com/?off=kb5l89qw)
