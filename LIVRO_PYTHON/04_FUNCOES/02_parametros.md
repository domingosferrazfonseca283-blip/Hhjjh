# Aula 02 — Parâmetros

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/04_02_parametros.svg)

## 1. Funções podem receber dados

Uma função pode receber informações.

```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Ana")
```

Aqui, `nome` é um parâmetro.

## 2. Parâmetro e argumento

Neste exemplo:

```python
def dobro(numero):
    print(numero * 2)

dobro(5)
```

- `numero` é o parâmetro;
- `5` é o argumento enviado na chamada.

## 3. Vários parâmetros

```python
def apresentar(nome, idade):
    print("Nome:", nome)
    print("Idade:", idade)

apresentar("João", 15)
```

A função recebe dois dados.

## Exercício guiado

Crie uma função `mostrar_pessoa(nome, cidade)`.

Ela deve mostrar:

```
Nome: ...
Cidade: ...
```

Chame a função com dados diferentes.

## Exercícios

1. Crie uma função que receba um número.
2. Crie uma função que receba dois números e mostre a soma.
3. Crie uma função que receba nome e idade.
4. Crie uma função que receba três notas.

## Desafio ⭐

Crie uma função `area_retangulo(largura, altura)` que calcule a área.

Por enquanto, apenas mostre o resultado.

## Revisão

- Parâmetros são entradas da função.
- Argumentos são os valores enviados.
- Uma função pode ter vários parâmetros.
- Cada parâmetro pode ser usado dentro do corpo da função.

**Assinatura:** Domingos Ferraz Fonseca
