# Aula 06 — Conjuntos com set

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/03_06_conjuntos.svg)

## 1. O que é um conjunto?

Um conjunto, chamado `set`, guarda valores únicos.

```python
numeros = {1, 2, 3, 4}
```

Se repetirmos um valor:

```python
numeros = {1, 2, 2, 3}
print(numeros)
```

O conjunto mantém apenas uma ocorrência de cada valor.

## 2. Adicionando

```python
numeros.add(5)
```

## 3. Removendo

```python
numeros.remove(2)
```

## 4. Por que usar conjuntos?

Eles são úteis quando queremos trabalhar com valores únicos e operações de conjunto.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
```

`|` representa união e `&` representa interseção.

## Exercício guiado

Crie dois conjuntos de números.

Descubra quais números aparecem nos dois usando interseção.

## Exercícios

1. Crie um conjunto com nomes repetidos e observe o resultado.
2. Adicione um item.
3. Remova um item.
4. Teste união.
5. Teste interseção.

## Desafio ⭐

Crie dois conjuntos de matérias estudadas por duas pessoas e descubra quais matérias as duas estudam.

## Revisão

- `set` guarda valores únicos.
- `add()` adiciona.
- `remove()` remove.
- União junta conjuntos.
- Interseção encontra valores presentes nos dois.

**Assinatura:** Domingos Ferraz Fonseca
