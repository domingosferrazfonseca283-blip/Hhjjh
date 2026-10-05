# Aula 07 — Condições dentro de condições

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/07_condicoes_aninhadas.svg)

## 1. O que significa aninhado?

Uma condição aninhada é uma condição dentro de outra condição.

Imagine duas portas:

1. primeiro você verifica se pode entrar;
2. depois verifica qual sala pode visitar.

Em Python:

```python
if primeira_condicao:
    if segunda_condicao:
        print("Tudo certo!")
```

A indentação mostra que o segundo `if` está dentro do primeiro.

## 2. Exemplo

```python
idade = 15
tem_permissao = True

if idade >= 13:
    print("Idade permitida.")
    
    if tem_permissao:
        print("Entrada autorizada.")
    else:
        print("Falta autorização.")
else:
    print("Idade não permitida.")
```

Primeiro o Python verifica a idade. Só depois verifica a autorização.

## 3. Cuidado com a indentação

Isto funciona:

```python
if idade >= 13:
    if tem_permissao:
        print("Pode entrar.")
```

A indentação faz parte da linguagem Python.

## Exercício guiado

Crie um programa com:

```python
idade = 16
tem_autorizacao = True
```

Primeiro verifique a idade. Se ela for suficiente, verifique a autorização.

Mostre mensagens diferentes para cada situação.

## Exercícios

1. Crie duas perguntas dentro de uma condição.
2. Faça um programa que primeiro verifique se um número é positivo e depois diga se ele é maior que 100.
3. Crie um programa que verifique se uma pessoa tem a idade mínima e, depois, se possui autorização.

## Desafio ⭐

Crie um "menu de decisões" simples. Primeiro pergunte se o usuário quer estudar. Se responder sim, pergunte qual assunto deseja estudar. Mostre uma mensagem diferente para cada escolha.

## Revisão

- Uma condição aninhada fica dentro de outra.
- A indentação mostra a hierarquia.
- O programa pode tomar uma decisão antes de tomar outra.
- Nem todo problema precisa de condições aninhadas; às vezes `and` deixa o código mais simples.

**Assinatura:** Domingos Ferraz Fonseca
