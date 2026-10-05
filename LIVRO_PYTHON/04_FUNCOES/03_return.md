# Aula 03 — return: devolvendo um resultado

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/04_03_return.svg)

## 1. Mostrar não é o mesmo que devolver

Veja:

```python
def dobro(numero):
    print(numero * 2)
```

A função mostra o resultado.

Com `return`, ela pode devolver o resultado para o programa:

```python
def dobro(numero):
    return numero * 2
```

Agora podemos guardar o resultado:

```python
resultado = dobro(5)
print(resultado)
```

## 2. Usando o resultado em outra conta

```python
def dobro(numero):
    return numero * 2

valor = dobro(6)
total = valor + 4
print(total)
```

## 3. Uma função pode devolver texto

```python
def criar_mensagem(nome):
    return "Olá, " + nome

mensagem = criar_mensagem("Ana")
print(mensagem)
```

## Exercício guiado

Crie:

```python
def somar(a, b):
    return a + b
```

Depois use o resultado em outra variável.

## Exercícios

1. Crie `triplo(numero)`.
2. Crie `subtrair(a, b)`.
3. Crie `media(a, b)`.
4. Crie uma função que devolva uma mensagem.

## Desafio ⭐

Crie uma calculadora com quatro funções:

- `somar`
- `subtrair`
- `multiplicar`
- `dividir`

Cada função deve devolver o resultado com `return`.

## Revisão

- `print()` mostra algo.
- `return` devolve um resultado.
- O resultado de uma função pode ser guardado em uma variável.
- Funções com `return` podem ser combinadas.

**Assinatura:** Domingos Ferraz Fonseca
