# Aula 02 — Percorrendo listas com for

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/03_02_listas_for.svg)

## 1. Uma lista e um loop

Podemos visitar cada item de uma lista usando `for`.

```python
nomes = ["Ana", "João", "Maria"]

for nome in nomes:
    print(nome)
```

O Python pega um nome por vez.

## 2. Fazendo cálculos

```python
notas = [7, 8, 9]

for nota in notas:
    print(nota + 1)
```

Podemos usar os itens para realizar cálculos.

## 3. Somando valores

```python
numeros = [10, 20, 30]
total = 0

for numero in numeros:
    total = total + numero

print(total)
```

## 4. Procurando um valor

```python
nomes = ["Ana", "João", "Maria"]

for nome in nomes:
    if nome == "João":
        print("Encontrado!")
```

## Exercício guiado

Crie uma lista com cinco números e use `for` para calcular a soma.

Depois mostre somente os números maiores que 10.

## Exercícios

1. Mostre todos os nomes de uma lista.
2. Conte quantos números são maiores que 20.
3. Calcule a soma de uma lista.
4. Mostre somente números pares.

## Desafio ⭐

Crie uma lista de notas e conte quantas são maiores ou iguais a 7.

## Revisão

- `for` percorre uma lista item por item.
- Podemos fazer cálculos durante o percurso.
- `if` pode ser usado dentro do `for`.
- Uma variável acumuladora pode guardar um total.

**Assinatura:** Domingos Ferraz Fonseca
