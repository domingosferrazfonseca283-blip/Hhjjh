# Aula 04 — Tuplas

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/03_04_tuplas.svg)

## 1. O que é uma tupla?

Uma tupla também guarda vários valores.

```python
coordenadas = (10, 20)
```

Ela se parece com uma lista, mas normalmente usamos uma tupla quando não queremos alterar seus itens.

## 2. Acessando valores

```python
coordenadas = (10, 20)

print(coordenadas[0])
print(coordenadas[1])
```

Assim como nas listas, a primeira posição é 0.

## 3. Tupla não é lista

Lista:

```python
cores = ["azul", "verde"]
```

Tupla:

```python
cores = ("azul", "verde")
```

A escolha depende do que queremos representar.

## Exercício guiado

Crie uma tupla com:

- nome de uma cidade;
- país;
- ano.

Depois mostre cada item.

## Exercícios

1. Crie uma tupla com três números.
2. Mostre o primeiro e o último.
3. Percorra uma tupla com `for`.
4. Explique, com suas palavras, a diferença entre lista e tupla.

## Desafio ⭐

Crie uma tupla chamada `produto` com nome, preço e código. Mostre os três dados.

## Revisão

- Tuplas guardam vários valores.
- Usamos parênteses na forma mais comum de criação.
- As posições começam em zero.
- Tuplas são apropriadas para dados que não precisam ser alterados.

**Assinatura:** Domingos Ferraz Fonseca
