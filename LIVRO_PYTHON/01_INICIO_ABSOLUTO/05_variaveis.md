# Aula 05 — Variáveis 📦

**Autor: Domingos Ferraz Fonseca**

## 1. O que é uma variável?

Uma variável é como uma pequena caixa com um nome.

Dentro dela podemos guardar um valor.

Exemplo:

```python
nome = "Ana"
idade = 10
```

Aqui temos duas caixas:

- `nome` guarda o texto `"Ana"`.
- `idade` guarda o número `10`.

Podemos usar esses valores depois:

```python
nome = "Ana"
idade = 10

print(nome)
print(idade)
```

## 2. Pense numa caixa

Imagine uma caixa com uma etiqueta.

A etiqueta diz:

**nome**

Dentro está:

**Ana**

O Python faz algo parecido quando escrevemos:

```python
nome = "Ana"
```

O sinal `=` significa, neste caso, **guardar um valor no nome**.

Não é uma igualdade de matemática.

## 3. Podemos trocar o valor

Uma variável pode receber outro valor.

```python
nome = "Ana"
print(nome)

nome = "Bruno"
print(nome)
```

Primeiro aparece Ana.

Depois aparece Bruno.

A caixa recebeu um novo valor.

## 4. Nomes simples ajudam muito

Prefira nomes fáceis de entender:

```python
nome = "Carlos"
idade = 12
cidade = "Luanda"
```

Evite nomes confusos quando está a aprender:

```python
x = "Carlos"
a = 12
z = "Luanda"
```

O código deve ser fácil de ler.

## 5. Texto, inteiro e decimal

Podemos guardar diferentes tipos de valores.

```python
nome = "Maria"
idade = 11
altura = 1.45
```

- `"Maria"` é texto.
- `11` é um número inteiro.
- `1.45` é um número decimal.

## 6. Uma conta com variáveis

```python
a = 5
b = 3
resultado = a + b

print(resultado)
```

O resultado será:

```
8
```

O Python pega nos valores guardados e faz a conta.

## 7. Exercício guiado

Cria três variáveis:

```python
nome = "..."
idade = ...
cidade = "..."
```

Depois escreve:

```python
print(nome)
print(idade)
print(cidade)
```

Troca os valores e executa novamente.

## 8. Exercícios

### Exercício 1
Cria uma variável chamada `animal` e guarda nela o nome de um animal.

### Exercício 2
Cria uma variável chamada `numero` e guarda nela o número 20.

### Exercício 3
Cria duas variáveis, soma-as e mostra o resultado.

### Exercício 4
Cria `nome` e `idade`. Mostra as duas.

### Exercício 5
Cria `preco1` e `preco2`. Calcula o total.

## 9. Desafio ⭐

Cria um pequeno cartão de apresentação:

```python
nome = "..."
idade = ...
cidade = "..."

print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)
```

## 10. Revisão

- Variável é um nome que usamos para guardar um valor.
- Podemos guardar texto e números.
- Podemos mudar o valor de uma variável.
- Nomes claros tornam o programa mais fácil de entender.
- Variáveis podem participar de contas.

**Assinatura:** Domingos Ferraz Fonseca
