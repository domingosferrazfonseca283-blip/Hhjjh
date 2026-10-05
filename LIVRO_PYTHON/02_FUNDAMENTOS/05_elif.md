# Aula 05 — Várias escolhas com elif

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/05_elif.svg)

## 1. O que é elif?

Às vezes, o programa precisa escolher entre várias possibilidades.

Já aprendemos:

- `if` = "se isso acontecer..."
- `else` = "caso contrário..."

Agora temos o `elif`, que significa uma nova condição.

A ideia é:

```python
if condição_1:
    # faça isto
elif condição_2:
    # faça aquilo
else:
    # faça outra coisa
```

O Python testa as condições de cima para baixo. Quando encontra uma condição verdadeira, executa aquele bloco e pula os outros.

## 2. Exemplo com notas

```python
nota = 8

if nota >= 9:
    print("Excelente!")
elif nota >= 7:
    print("Muito bom!")
elif nota >= 5:
    print("Pode melhorar.")
else:
    print("Vamos estudar mais.")
```

Como `nota` vale 8, o programa imprime:

```
Muito bom!
```

## 3. Por que a ordem importa?

Veja:

```python
idade = 15

if idade >= 18:
    print("Adulto")
elif idade >= 13:
    print("Adolescente")
else:
    print("Criança")
```

A ordem começa pela condição mais específica para aquele exemplo.

## Exercício guiado

Crie um programa que receba uma nota e mostre:

- 9 ou 10: "Excelente"
- 7 ou 8: "Muito bom"
- 5 ou 6: "Regular"
- abaixo de 5: "Precisa estudar"

Teste com pelo menos quatro notas.

## Exercícios

1. Faça um programa que diga se uma pessoa é criança, adolescente ou adulta.
2. Faça um programa que receba um número e diga se ele é positivo, negativo ou zero.
3. Faça um programa que receba a temperatura e mostre uma mensagem para frio, agradável ou quente.

## Desafio ⭐

Crie um pequeno classificador de livros:

- nota 9 ou 10 → "Favorito"
- nota 7 ou 8 → "Muito bom"
- nota 5 ou 6 → "Bom"
- abaixo de 5 → "Pode escolher outro"

## Revisão

- `elif` adiciona outra condição.
- Podemos usar vários `elif`.
- O Python para no primeiro bloco verdadeiro.
- A indentação define o bloco de cada condição.

**Assinatura:** Domingos Ferraz Fonseca
