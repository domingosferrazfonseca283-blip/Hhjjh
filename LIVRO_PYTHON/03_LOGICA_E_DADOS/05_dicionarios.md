# Aula 05 — Dicionários

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/03_05_dicionarios.svg)

## 1. O que é um dicionário?

Um dicionário guarda dados usando uma chave e um valor.

```python
pessoa = {
    "nome": "Ana",
    "idade": 15
}
```

Pense assim:

- chave = etiqueta;
- valor = informação.

## 2. Acessando um valor

```python
print(pessoa["nome"])
print(pessoa["idade"])
```

## 3. Alterando um valor

```python
pessoa["idade"] = 16
```

## 4. Adicionando uma chave

```python
pessoa["cidade"] = "Luanda"
```

## 5. Percorrendo um dicionário

```python
for chave, valor in pessoa.items():
    print(chave, valor)
```

## Exercício guiado

Crie um dicionário de estudante com:

- nome;
- idade;
- curso;
- nota.

Mostre cada informação.

## Exercícios

1. Crie um dicionário de um livro.
2. Adicione uma nova informação.
3. Altere uma informação.
4. Percorra o dicionário com `items()`.

## Desafio ⭐

Crie um cadastro simples de produto com nome, preço, quantidade e categoria. Depois mostre todos os dados.

## Revisão

- Dicionários trabalham com chave e valor.
- Uma chave identifica uma informação.
- Podemos adicionar e alterar valores.
- `items()` permite percorrer chave e valor.

**Assinatura:** Domingos Ferraz Fonseca
