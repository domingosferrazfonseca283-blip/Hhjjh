# Model Registry

**Assinatura:** Domingos Ferraz Fonseca

## O que vamos aprender

Um Model Registry é um catálogo onde guardamos versões dos modelos, estados e informações importantes.

**Mapa da aula:** treino → modelo v1 → testes → aprovado → produção

![Diagrama da aula](../IMAGENS/18_03_registry.svg)

## Ideia principal

Quando temos muitos modelos, guardar ficheiros soltos torna-se confuso. Um Model Registry funciona como uma biblioteca organizada de modelos. Podemos guardar a versão, métricas, origem e estado do modelo.

Estados comuns podem ser desenvolvimento, candidato e produção.

## Exemplo em Python

~~~python
modelo = {"versao": "v2", "acuracia": 0.91, "estado": "candidato"}
if modelo["acuracia"] >= 0.90:
    modelo["estado"] = "aprovado"
print(modelo)
~~~

O exemplo é pequeno de propósito. Em sistemas reais, cada etapa pode ser implementada por várias ferramentas, mas a ideia fundamental continua a mesma: **controlar o ciclo de vida do modelo**.

## Exercício guiado

1. Leia o exemplo.
2. Identifique a entrada e a saída.
3. Altere pelo menos um valor.
4. Execute novamente.
5. Explique com as suas palavras o que mudou.

**Tarefa:** Crie três versões fictícias de um modelo e escolha a aprovada.

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