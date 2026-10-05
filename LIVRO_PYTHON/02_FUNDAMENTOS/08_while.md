# Aula 08 — Repetição com while

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/08_while.svg)

## 1. O que é repetição?

Imagine dizer:

> "Enquanto a condição for verdadeira, continue."

É exatamente a ideia do `while`.

```python
while condição:
    # repita
```

## 2. Contando

```python
contador = 1

while contador <= 5:
    print(contador)
    contador = contador + 1
```

O resultado é:

```
1
2
3
4
5
```

A cada volta, o contador aumenta.

## 3. Por que mudar a variável?

Se a condição continuar verdadeira para sempre, o programa pode ficar preso em um loop infinito.

Por isso, em muitos loops `while`, alguma variável precisa mudar.

## Exercício guiado

Faça um programa que conte de 1 até 10.

Depois faça outro que conte de 10 até 1.

## 4. while com input

Podemos pedir dados ao usuário:

```python
resposta = ""

while resposta != "sim":
    resposta = input("Digite sim para continuar: ")

print("Continuando!")
```

## Exercícios

1. Conte de 1 até 20.
2. Mostre apenas os números pares de 2 até 20.
3. Faça uma contagem regressiva de 10 até 1.
4. Peça uma palavra até o usuário digitar "python".

## Desafio ⭐

Crie um programa que tenha um contador de pontos.

Comece em zero e repita cinco vezes, aumentando um ponto a cada rodada. No final, mostre a pontuação.

## Revisão

- `while` repete enquanto uma condição for verdadeira.
- A condição é testada a cada volta.
- Uma variável pode controlar o número de repetições.
- É importante evitar loops infinitos acidentais.

**Assinatura:** Domingos Ferraz Fonseca
