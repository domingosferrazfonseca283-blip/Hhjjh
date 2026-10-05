# Aula 07 — Erros e mensagens 🚦

**Autor: Domingos Ferraz Fonseca**

![Diagrama da aula](../../IMAGENS/07_erro_mensagem.svg)

## 1. Errar faz parte

Quando estamos a aprender Python, vamos encontrar erros.

Isso é normal.

Um erro não significa que não conseguimos aprender.

O erro é uma mensagem que tenta ajudar.

## 2. Um erro simples

Veja:

```python
print("Olá)
```

O texto começou com uma aspa, mas não terminou corretamente.

O Python vai mostrar uma mensagem de erro.

A ideia principal é:

**ler → encontrar → corrigir → testar novamente**

## 3. Outro exemplo

```python
numero = int("abc")
```

Aqui pedimos ao Python para transformar `"abc"` em número.

Mas `abc` não é um número.

O Python avisa que não consegue fazer essa conversão.

## 4. Erros de escrita

Python precisa que escrevamos os comandos corretamente.

Isto:

```python
prit("Olá")
```

está errado.

O nome correto é:

```python
print("Olá")
```

Uma letra errada pode mudar tudo.

## 5. Como estudar um erro

Quando aparecer um erro:

1. Respira.
2. Lê a última parte da mensagem.
3. Olha para a linha indicada.
4. Compara com o exemplo correto.
5. Corrige uma coisa de cada vez.
6. Executa novamente.

## 6. Exercício guiado

Corrige estes programas:

### Programa A

```python
print("Bom dia)
```

### Programa B

```python
prit("Olá")
```

### Programa C

```python
idade = int("dez")
print(idade)
```

Depois explica, com as tuas palavras, qual era o problema.

## 7. Exercícios

### Exercício 1
Escreve um `print()` correto.

### Exercício 2
Cria uma variável chamada `nome` e mostra-a.

### Exercício 3
Pede um número inteiro usando `int(input())`.

### Exercício 4
Escreve de propósito um pequeno erro de escrita. Depois corrige-o.

### Exercício 5
Explica por que razão uma mensagem de erro pode ser útil.

## 8. Desafio ⭐

Cria um programa pequeno e testa-o.

Depois provoca um erro simples, observa a mensagem e corrige o programa.

**Objetivo:** aprender que corrigir erros é uma parte normal da programação.

## 9. Revisão

- Erros acontecem.
- Mensagens de erro ajudam.
- Devemos ler a mensagem com calma.
- A linha indicada é uma pista importante.
- Corrigir e testar faz parte do trabalho de programar.

**Assinatura:** Domingos Ferraz Fonseca
