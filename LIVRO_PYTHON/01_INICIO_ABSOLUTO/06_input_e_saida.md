# Aula 06 — Entrada e saída ⌨️

**Autor: Domingos Ferraz Fonseca**

![Diagrama da aula](../../IMAGENS/06_input_e_saida.svg)

## 1. O computador também pode ouvir

Até agora nós mandámos o Python mostrar coisas.

Agora vamos fazer o programa receber uma resposta da pessoa.

Usamos:

```python
input()
```

Exemplo:

```python
nome = input("Qual é o teu nome? ")
print("Olá,", nome)
```

O programa pergunta.

A pessoa responde.

O Python guarda a resposta.

Depois o programa mostra uma mensagem.

## 2. O caminho da informação

Pensa assim:

**Pessoa → input() → variável → print() → pessoa**

A pessoa escreve uma resposta.

O programa recebe a resposta.

Uma variável pode guardar essa resposta.

Depois `print()` mostra o resultado.

## 3. Atenção: input recebe texto

Este programa:

```python
idade = input("Qual é a tua idade? ")
```

guarda a resposta como texto.

Se a pessoa escrever `12`, o Python recebe o texto `"12"`.

Para transformar esse texto em inteiro, podemos usar:

```python
idade = int(input("Qual é a tua idade? "))
```

Agora podemos fazer contas com a idade.

## 4. Exemplo completo

```python
nome = input("Nome: ")
idade = int(input("Idade: "))

print("Olá,", nome)
print("No próximo ano terás", idade + 1)
```

## 5. Números decimais

Para receber um número decimal:

```python
altura = float(input("Altura: "))
```

O `float()` transforma a resposta num número decimal.

## 6. Exercício guiado

Cria um programa que pergunte:

- nome;
- cidade;
- idade.

Depois mostra as respostas.

Começa assim:

```python
nome = input("Nome: ")
cidade = input("Cidade: ")
idade = int(input("Idade: "))

print("Nome:", nome)
print("Cidade:", cidade)
print("Idade:", idade)
```

## 7. Exercícios

### Exercício 1
Pergunta o nome e mostra uma saudação.

### Exercício 2
Pergunta a idade e mostra a idade no próximo ano.

### Exercício 3
Pede dois números inteiros e soma-os.

### Exercício 4
Pede dois números e calcula a multiplicação.

### Exercício 5
Pede o nome de uma comida e diz que é uma escolha interessante.

## 8. Desafio ⭐

Cria um programa chamado **Mini Perfil**.

Ele deve perguntar:

- nome;
- idade;
- cidade;
- comida favorita.

Depois deve mostrar tudo de forma organizada.

## 9. Revisão

- `input()` recebe informação.
- A resposta de `input()` é texto.
- `int()` transforma texto num inteiro.
- `float()` transforma texto num decimal.
- `print()` mostra informação.

**Assinatura:** Domingos Ferraz Fonseca
