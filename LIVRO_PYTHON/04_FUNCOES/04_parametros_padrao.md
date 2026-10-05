# Aula 04 — Parâmetros com valores padrão

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/04_04_parametros_padrao.svg)

## 1. Um valor que já vem pronto

Podemos dar um valor padrão a um parâmetro.

```python
def saudacao(nome="amigo"):
    print("Olá,", nome)
```

Se não enviarmos um nome:

```python
saudacao()
```

O programa usa `"amigo"`.

Se enviarmos:

```python
saudacao("Ana")
```

O valor enviado substitui o padrão.

## 2. Por que isso é útil?

Valores padrão tornam algumas funções mais fáceis de usar.

```python
def potencia(numero, expoente=2):
    return numero ** expoente
```

Agora:

```python
print(potencia(5))
print(potencia(5, 3))
```

## Exercício guiado

Crie uma função:

```python
def apresentar(nome="visitante"):
    ...
```

Teste com e sem argumento.

## Exercícios

1. Crie uma função com uma mensagem padrão.
2. Crie uma função de potência com expoente padrão 2.
3. Crie uma função que tenha dois parâmetros e um deles tenha valor padrão.

## Desafio ⭐

Crie uma função para calcular o preço de um produto com uma taxa padrão.

## Revisão

- Um parâmetro pode ter valor padrão.
- O valor padrão é usado quando nenhum argumento é enviado.
- Um argumento enviado pode substituir o padrão.

**Assinatura:** Domingos Ferraz Fonseca
