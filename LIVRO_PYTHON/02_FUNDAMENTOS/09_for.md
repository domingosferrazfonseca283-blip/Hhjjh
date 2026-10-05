# Aula 09 — Repetição com for

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/09_for.svg)

## 1. O que é for?

O `for` é usado quando queremos repetir algo para cada item de uma sequência ou para uma quantidade conhecida de vezes.

Exemplo:

```python
for numero in range(5):
    print(numero)
```

O resultado começa em zero:

```
0
1
2
3
4
```

## 2. Entendendo range()

`range(5)` cria uma sequência de números de 0 até 4.

Para começar em 1:

```python
for numero in range(1, 6):
    print(numero)
```

Resultado:

```
1
2
3
4
5
```

O último número indicado não entra na sequência.

## 3. Percorrendo textos

Também podemos percorrer uma palavra:

```python
for letra in "Python":
    print(letra)
```

O programa visita uma letra de cada vez.

## Exercício guiado

Faça um programa que mostre os números de 1 até 10 usando `for` e `range()`.

Depois mostre apenas os números pares usando uma condição.

## Exercícios

1. Conte de 1 até 20 com `for`.
2. Mostre cada letra do seu nome.
3. Mostre a tabuada de um número escolhido.
4. Calcule a soma dos números de 1 até 10.

## Desafio ⭐

Crie um programa que peça uma palavra e mostre cada letra numerada:

```
1 - P
2 - y
3 - t
...
```

## Revisão

- `for` repete para cada item de uma sequência.
- `range()` é muito usado para criar sequências de números.
- O último valor de `range(início, fim)` fica de fora.
- `for` também pode percorrer textos.

**Assinatura:** Domingos Ferraz Fonseca
