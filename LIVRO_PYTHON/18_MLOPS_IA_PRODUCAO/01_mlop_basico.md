# MLOps básico

**Assinatura:** Domingos Ferraz Fonseca

## O que vamos aprender

MLOps junta desenvolvimento de software, dados e Machine Learning para colocar modelos em produção com segurança e organização.

**Mapa da aula:** ideia → dados → treino → modelo → API → monitorização

![Diagrama da aula](../IMAGENS/18_01_mlop.svg)

## Ideia principal

Imagine que treinamos um modelo no computador e ele funciona muito bem. O trabalho não termina aí. Quando o modelo chega a uma aplicação real, precisamos saber qual versão foi usada, como foi treinado, se está rápido e se continua a funcionar bem.

MLOps é a disciplina que organiza esse caminho. Não é uma biblioteca única: é uma forma de trabalhar.

## Exemplo em Python

~~~python
pipeline = ["dados", "treino", "validação", "deploy", "monitorização"]
for etapa in pipeline:
    print(etapa)
~~~

O exemplo é pequeno de propósito. Em sistemas reais, cada etapa pode ser implementada por várias ferramentas, mas a ideia fundamental continua a mesma: **controlar o ciclo de vida do modelo**.

## Exercício guiado

1. Leia o exemplo.
2. Identifique a entrada e a saída.
3. Altere pelo menos um valor.
4. Execute novamente.
5. Explique com as suas palavras o que mudou.

**Tarefa:** Desenhe no papel o ciclo MLOps da aula.

## Exercícios

1. Explique por que um modelo em produção precisa de acompanhamento.
2. Dê um exemplo de informação que deve ser versionada.
3. Imagine um problema que poderia acontecer sem validação.
4. Desenhe uma pequena pipeline com pelo menos quatro etapas.

## Desafio

Crie no papel ou em Python uma pequena pipeline com **dados → treino → validação → produção → monitorização**. Depois escreva uma frase explicando a responsabilidade de cada etapa.

## Boas práticas

- Registe versões de código, dados e modelos.
- Automatize verificações repetitivas.
- Não coloque segredos diretamente no código.
- Registe métricas importantes.
- Tenha uma forma clara de voltar a uma versão anterior.
- Documente decisões técnicas.

## Revisão

MLOps trata do ciclo de vida do Machine Learning. O modelo precisa ser treinado, validado, disponibilizado e acompanhado. Quanto mais claro for esse processo, mais fácil será manter o sistema confiável.

**Pergunta final:** se o modelo piorar amanhã, você conseguiria descobrir **qual modelo estava em produção, com quais dados foi treinado e qual código o criou**?