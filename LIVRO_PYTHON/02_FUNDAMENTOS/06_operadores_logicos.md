# Aula 06 — Operadores lógicos: and, or e not

**Assinatura:** Domingos Ferraz Fonseca

![Diagrama da aula](../../IMAGENS/06_operadores_logicos.svg)

## 1. O que são operadores lógicos?

Eles permitem juntar ou inverter condições.

Os três principais são:

- `and` = e
- `or` = ou
- `not` = não

Pense em pequenas perguntas.

Com `and`, as duas precisam ser verdadeiras.

```python
idade = 15
tem_autorizacao = True

print(idade >= 13 and tem_autorizacao)
```

Resultado:

```
True
```

## 2. O operador and

`and` exige que todas as condições sejam verdadeiras.

```python
idade = 15
tem_carteirinha = True

if idade >= 13 and tem_carteirinha:
    print("Pode entrar.")
else:
    print("Não pode entrar.")
```

Se uma das condições for falsa, o resultado do `and` será falso.

## 3. O operador or

`or` aceita quando pelo menos uma condição é verdadeira.

```python
dia = "sábado"

if dia == "sábado" or dia == "domingo":
    print("É fim de semana!")
```

## 4. O operador not

`not` inverte o valor lógico.

```python
chovendo = False

if not chovendo:
    print("Podemos continuar.")
```

## Exercício guiado

Crie um programa que tenha:

```python
idade = 14
tem_permissao = True
```

Use `and` para mostrar "Pode participar" somente quando a idade for pelo menos 13 e houver permissão.

Depois altere os valores e observe o resultado.

## Exercícios

1. Use `and` para verificar se um número está entre 10 e 20.
2. Use `or` para verificar se uma palavra é "sim" ou "s".
3. Use `not` para testar uma variável booleana.
4. Crie uma condição que exija duas respostas corretas.

## Desafio ⭐

Faça um programa que verifique três coisas:

- a pessoa tem idade suficiente;
- tem autorização;
- não está bloqueada.

Use `and` e `not` para montar a condição.

## Revisão

- `and` significa "e".
- `or` significa "ou".
- `not` significa "não" e inverte o valor lógico.
- Operadores lógicos ajudam o programa a tomar decisões mais inteligentes.

**Assinatura:** Domingos Ferraz Fonseca
