# Aula 04 — Decisões com if e else 🚦

**Autor: Domingos Ferraz Fonseca**

![Fluxo de uma decisão](../../IMAGENS/04_if_else.svg)

## 1. Um programa pode escolher

Um programa pode verificar uma condição.

Exemplo:

```python
idade = 12

if idade >= 10:
    print("Tens 10 anos ou mais.")
```

A palavra `if` significa, de forma simples:

**se isto acontecer, faz isto.**

## 2. O else

Podemos indicar o que acontece quando a condição não é verdadeira.

```python
idade = 8

if idade >= 10:
    print("Tens 10 anos ou mais.")
else:
    print("Tens menos de 10 anos.")
```

## 3. A indentação

Observe os espaços:

```python
if idade >= 10:
    print("Olá")
```

A linha do `print` pertence ao `if`.

Em Python, a indentação é importante.

## 4. Exercícios

1. Verifica se um número é maior que 10.
2. Verifica se uma pessoa tem 18 anos ou mais.
3. Verifica se um número é positivo.
4. Usa `if` e `else` para mostrar duas mensagens diferentes.

## Desafio ⭐

Cria um programa que peça um número e diga:

- "É positivo" se for maior que zero;
- "Não é positivo" caso contrário.

## Revisão

- `if` toma uma decisão.
- `else` trata o outro caminho.
- A condição precisa ser verdadeira ou falsa.
- A indentação organiza o código.

**Assinatura:** Domingos Ferraz Fonseca
