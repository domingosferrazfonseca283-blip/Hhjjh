# Aula 03 — Métodos importantes de listas

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/03_03_metodos_listas.svg)

## 1. O que é um método?

Um método é uma ação que podemos pedir a um objeto.

Listas possuem vários métodos úteis.

## 2. append()

Adiciona no final:

```python
numeros = [1, 2, 3]
numeros.append(4)
```

## 3. insert()

Adiciona em uma posição:

```python
nomes = ["Ana", "Carlos"]
nomes.insert(1, "Bruno")
```

## 4. remove()

Remove um valor:

```python
frutas = ["maçã", "banana", "uva"]
frutas.remove("banana")
```

## 5. pop()

Remove usando uma posição:

```python
frutas.pop(0)
```

## 6. sort()

Organiza valores:

```python
numeros = [5, 2, 8, 1]
numeros.sort()
print(numeros)
```

## Exercício guiado

Crie uma lista de cinco números.

- adicione um número;
- insira outro no início;
- remova um número;
- organize a lista.

## Exercícios

1. Teste `append()`.
2. Teste `insert()`.
3. Teste `remove()`.
4. Teste `pop()`.
5. Teste `sort()`.

## Desafio ⭐

Crie uma lista de tarefas. Adicione tarefas, remova uma tarefa concluída e organize a lista.

## Revisão

- Métodos são ações disponíveis para objetos.
- Listas possuem métodos para adicionar, remover e organizar itens.
- Sempre confira qual posição você está alterando.

**Assinatura:** Domingos Ferraz Fonseca
