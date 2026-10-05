# Reprodutibilidade

**Assinatura:** Domingos Ferraz Fonseca

## O que vamos aprender

Um experimento é reprodutível quando conseguimos reconstruir o mesmo processo usando versões conhecidas de código, dados e dependências.

**Mapa da aula:** configuração + versões + sementes → experimento repetível

![Diagrama da aula](../IMAGENS/18_06_reprodutibilidade.svg)

## Ideia principal

Reprodutibilidade significa conseguir reconstruir um experimento. Para isso devemos registar versões, configurações, dados usados e dependências.

Uma boa prática é transformar configurações importantes em ficheiros e evitar depender de alterações manuais escondidas.

## Exemplo em Python

~~~python
config = {"seed": 42, "dados": "v2", "modelo": "v3"}
print(config)
~~~

O exemplo é pequeno de propósito. Em sistemas reais, cada etapa pode ser implementada por várias ferramentas, mas a ideia fundamental continua a mesma: **controlar o ciclo de vida do modelo**.

## Exercício guiado

1. Leia o exemplo.
2. Identifique a entrada e a saída.
3. Altere pelo menos um valor.
4. Execute novamente.
5. Explique com as suas palavras o que mudou.

**Tarefa:** Crie uma configuração com versão de dados, modelo e seed.

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