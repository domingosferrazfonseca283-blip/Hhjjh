# Aula 06 — Funções trabalhando com listas

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/04_06_funcoes_listas.svg)

## 1. Função + lista

Podemos enviar uma lista para uma função.

```python
def mostrar_itens(itens):
    for item in itens:
        print(item)

frutas = ["maçã", "banana", "uva"]
mostrar_itens(frutas)
```

## 2. Calculando dentro da função

```python
def somar_lista(numeros):
    total = 0

    for numero in numeros:
        total = total + numero

    return total
```

Uso:

```python
print(somar_lista([10, 20, 30]))
```

## 3. Criando funções reutilizáveis

Podemos criar funções para tarefas comuns:

```python
def contar_itens(itens):
    return len(itens)
```

## Exercício guiado

Crie uma função que receba uma lista de números e devolva a soma.

Depois crie outra que devolva quantos itens existem.

## Exercícios

1. Função que encontre o maior valor.
2. Função que conte números pares.
3. Função que mostre todos os itens.
4. Função que calcule a média.

## Desafio ⭐

Crie um pequeno analisador de notas que receba uma lista e devolva:

- quantidade de notas;
- soma;
- média;
- maior nota;
- menor nota.

## Revisão

- Funções podem receber listas.
- Podemos usar `for` dentro de funções.
- `return` permite devolver resultados calculados.
- Funções reutilizáveis reduzem repetição.

**Assinatura:** Domingos Ferraz Fonseca
