# Aula 5 — Testes de integração

**Assinatura:** Domingos Ferraz Fonseca

## 1. Teste unitário versus integração

Um teste unitário normalmente verifica uma unidade pequena e isolada.

Um teste de integração verifica se várias partes funcionam juntas.

![Testes de integração](../IMAGENS/13_05_integracao.svg)

## 2. Exemplo

Imagine:

~~~text
serviço → repositório → SQLite
~~~

Um teste de integração pode verificar o fluxo completo usando um banco apropriado para testes.

## 3. Pirâmide de testes

Uma estratégia comum possui:

- muitos testes unitários;
- menos testes de integração;
- poucos testes de ponta a ponta.

Cada tipo tem um objetivo.

## Exercício guiado

Escolha uma funcionalidade e escreva:

1. um teste unitário;
2. um teste de integração.

## Exercícios

1. Explique a diferença entre os testes.
2. Identifique uma integração do seu projeto.
3. Crie um teste de integração.
4. Faça o teste usar dados isolados.

## Desafio

Crie uma pequena suíte que teste serviço + repositório.

## Boas práticas

Testes de integração devem ser repetíveis e não depender de dados pessoais ou externos imprevisíveis.

## Revisão

Testes de integração aumentam a confiança de que diferentes componentes realmente funcionam juntos.
