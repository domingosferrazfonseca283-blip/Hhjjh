# Aula 05 — Escopo de variáveis

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/04_05_escopo.svg)

## 1. Onde uma variável existe?

Escopo é a região do programa onde uma variável pode ser usada.

Veja:

```python
def mostrar():
    mensagem = "Olá"
    print(mensagem)

mostrar()
```

A variável `mensagem` foi criada dentro da função.

## 2. Variável local

Uma variável criada dentro de uma função normalmente é local àquela função.

```python
def calcular():
    numero = 10
    return numero

print(calcular())
```

É melhor pensar nas variáveis locais como pertencentes ao trabalho daquela função.

## 3. Variáveis fora da função

```python
nome = "Ana"

def mostrar():
    print(nome)

mostrar()
```

O Python consegue acessar essa variável externa neste exemplo, mas devemos ter cuidado para não criar dependências desnecessárias.

## Exercício guiado

Crie uma função com uma variável local e devolva seu valor usando `return`.

Depois tente explicar por que uma variável criada dentro de uma função não deve ser tratada como se fosse automaticamente uma variável global.

## Exercícios

1. Crie duas funções com variáveis locais de mesmo nome.
2. Observe que cada função pode ter seu próprio valor.
3. Use parâmetros e `return` em vez de depender de variáveis globais.

## Desafio ⭐

Reescreva um pequeno programa para que suas funções recebam dados por parâmetros e devolvam resultados por `return`, evitando variáveis globais sempre que possível.

## Revisão

- Escopo indica onde um nome pode ser usado.
- Variáveis dentro de funções normalmente são locais.
- Parâmetros e `return` ajudam a controlar a comunicação entre funções.

**Assinatura:** Domingos Ferraz Fonseca
