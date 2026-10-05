# Aula 10 — Revisão: decisões e ciclos

**Assinatura:** Domingos Ferraz Fonseca

![Mapa da aula](../../IMAGENS/10_mapa_decisoes_ciclos.svg)

## 1. O que aprendemos?

Agora já conhecemos ferramentas para fazer programas que pensam e repetem tarefas:

- `if`
- `elif`
- `else`
- `and`
- `or`
- `not`
- condições aninhadas
- `while`
- `for`
- `range()`

## 2. Exercício de revisão

Crie um programa que peça uma nota.

Depois:

- use `if`, `elif` e `else`;
- mostre uma mensagem de acordo com a nota;
- repita o processo três vezes usando `for`.

Uma possível estrutura é:

```python
for tentativa in range(3):
    nota = float(input("Digite a nota: "))

    if nota >= 9:
        print("Excelente!")
    elif nota >= 7:
        print("Muito bom!")
    elif nota >= 5:
        print("Regular.")
    else:
        print("Vamos estudar mais.")
```

## 3. Mini-projeto: contador de estudos

Crie um programa que pergunte quantos exercícios a pessoa quer fazer.

Use `while` para contar os exercícios concluídos.

O programa pode mostrar:

```
Exercício 1 concluído!
Exercício 2 concluído!
Exercício 3 concluído!
```

No final:

```
Parabéns! Você terminou.
```

## Desafios ⭐

### Desafio 1 — Tabuada

Peça um número e mostre sua tabuada de 1 a 10.

### Desafio 2 — Número secreto

Escolha um número fixo no código. Peça tentativas ao usuário usando `while` até acertar.

### Desafio 3 — Menu

Mostre três opções e use `if`/ `elif` / `else` para responder à escolha.

## Checklist

Antes de avançar, veja se consegue:

- [ ] criar uma decisão com `if`;
- [ ] adicionar alternativas com `elif`;
- [ ] usar `else`;
- [ ] combinar condições com `and` e `or`;
- [ ] inverter uma condição com `not`;
- [ ] criar um `while`;
- [ ] criar um `for`;
- [ ] usar `range()`.

Se ainda houver dúvidas, volte às aulas anteriores e refaça os exercícios.

**Assinatura:** Domingos Ferraz Fonseca
