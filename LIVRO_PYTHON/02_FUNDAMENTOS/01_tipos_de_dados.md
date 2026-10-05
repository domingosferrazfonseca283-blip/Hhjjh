# Aula 01 — Tipos de dados 🧩

**Autor: Domingos Ferraz Fonseca**

![Diagrama dos tipos de dados](../../IMAGENS/01_tipos_de_dados.svg)

## 1. O que é um tipo de dado?

Um dado é uma informação.

Em Python, diferentes informações podem ter diferentes tipos.

Os quatro tipos que vamos conhecer primeiro são:

- `str` — texto;
- `int` — número inteiro;
- `float` — número decimal;
- `bool` — verdadeiro ou falso.

## 2. Texto

Texto é chamado de `str`.

```python
nome = "Ana"
cidade = "Luanda"
```

As aspas mostram que estamos a guardar texto.

## 3. Número inteiro

Um número inteiro não tem parte decimal.

```python
idade = 12
ano = 2026
```

## 4. Número decimal

Um número decimal pode ter uma parte depois do ponto.

```python
preco = 10.5
altura = 1.45
```

Em Python usamos ponto para o decimal.

## 5. Verdadeiro ou falso

O tipo `bool` tem dois valores principais:

```python
True
False
```

Exemplo:

```python
tem_chuva = True
```

## 6. Descobrir o tipo

Podemos usar `type()`:

```python
nome = "Ana"
idade = 12

print(type(nome))
print(type(idade))
```

## 7. Exercícios

1. Cria uma variável de texto.
2. Cria uma variável inteira.
3. Cria uma variável decimal.
4. Cria uma variável com `True`.
5. Usa `type()` para descobrir os tipos.

## Desafio ⭐

Cria um pequeno cartão com quatro informações, usando pelo menos três tipos diferentes.

## Revisão

- `str` é texto.
- `int` é inteiro.
- `float` é decimal.
- `bool` representa verdadeiro ou falso.
- `type()` ajuda a descobrir o tipo.

**Assinatura:** Domingos Ferraz Fonseca
