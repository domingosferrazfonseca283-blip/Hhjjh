# Aula 01 — Listas: guardando vários valores

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/03_01_listas.svg)

## 1. O que é uma lista?

Uma lista guarda vários valores em uma única variável.

```python
frutas = ["maçã", "banana", "laranja"]
```

Imagine uma caixa com vários espaços. Cada espaço guarda um item.

## 2. Posições

O Python começa a contar as posições pelo número zero.

```python
frutas = ["maçã", "banana", "laranja"]

print(frutas[0])
print(frutas[1])
```

Resultado:

```
maçã
banana
```

## 3. Alterando um item

```python
frutas[1] = "uva"
print(frutas)
```

A lista agora contém "uva" no lugar de "banana".

## 4. Adicionando itens

```python
frutas.append("manga")
```

O método `append()` coloca um item no final.

## 5. Quantos itens existem?

```python
print(len(frutas))
```

`len()` informa o tamanho da lista.

## Exercício guiado

Crie uma lista com cinco animais. Mostre:

1. o primeiro animal;
2. o último animal;
3. a quantidade de animais.

## Exercícios

1. Crie uma lista com cinco nomes.
2. Troque o segundo nome.
3. Adicione mais dois nomes.
4. Mostre cada item usando `for`.

## Desafio ⭐

Crie uma lista de matérias escolares e faça um programa que mostre cada matéria numerada.

## Revisão

- Listas guardam vários valores.
- A primeira posição é 0.
- `append()` adiciona um item.
- `len()` conta os itens.

**Assinatura:** Domingos Ferraz Fonseca
