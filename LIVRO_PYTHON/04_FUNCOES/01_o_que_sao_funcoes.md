# Aula 01 — O que são funções?

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/04_01_funcoes.svg)

## 1. Uma função é uma tarefa organizada

Uma função é um bloco de código criado para realizar uma tarefa.

Imagine uma máquina: você entrega algo para ela, ela trabalha e pode devolver um resultado.

```python
def dizer_ola():
    print("Olá!")
```

Para executar:

```python
dizer_ola()
```

## 2. Por que usar funções?

Sem funções, podemos repetir o mesmo código muitas vezes.

Com uma função, escrevemos a tarefa uma vez e podemos chamá-la várias vezes.

```python
def mostrar_mensagem():
    print("Estude Python!")

mostrar_mensagem()
mostrar_mensagem()
```

## 3. Criando uma função

A palavra `def` começa uma definição de função.

```python
def nome_da_funcao():
    print("Faz alguma coisa")
```

Os parênteses fazem parte da definição e a indentação mostra o corpo da função.

## Exercício guiado

Crie três funções:

- `saudacao()`
- `mostrar_nome()`
- `mostrar_linguagem()`

Depois chame cada uma.

## Exercícios

1. Crie uma função que mostre seu nome.
2. Crie uma função que mostre uma frase.
3. Chame uma função cinco vezes.
4. Crie uma função que mostre três linhas.

## Desafio ⭐

Crie uma função chamada `inicio_do_estudo()` que mostre três mensagens motivadoras para começar uma sessão de Python.

## Revisão

- Funções organizam tarefas.
- `def` cria uma função.
- O código indentado pertence à função.
- Chamamos uma função usando seu nome e parênteses.

**Assinatura:** Domingos Ferraz Fonseca
