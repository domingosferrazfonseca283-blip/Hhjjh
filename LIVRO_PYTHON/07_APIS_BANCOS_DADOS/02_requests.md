# Aula 2 — Fazendo pedidos HTTP com requests

**Assinatura:** Domingos Ferraz Fonseca

## 1. Entendendo a ideia

O módulo requests facilita pedidos HTTP. Em projetos reais, uma API pode responder com JSON, texto ou outros formatos.

![Diagrama da aula](../IMAGENS/07_02_requests.svg)

## 2. Exemplo prático

~~~python
import requests

resposta = requests.get("https://example.com")
print(resposta.status_code)
~~~

> **Nota:** URLs e serviços externos podem mudar. Use APIs de teste ou documentação oficial quando executar os exemplos.

## 3. Exercício guiado

1. Instale requests quando necessário. 2. Faça um GET para uma URL de teste. 3. Mostre o status recebido.

## 4. Exercícios

1. Explique o conceito principal com suas próprias palavras.
2. Faça uma pequena alteração no exemplo.
3. Crie um exemplo relacionado com uma situação do dia a dia.
4. Registe o resultado que observou.

## 5. Desafio

Crie uma função que faça um GET e mostre o status da resposta.

## 6. Boas práticas

- Leia a documentação da biblioteca ou API usada.
- Não coloque senhas ou chaves secretas diretamente no código.
- Valide dados recebidos de fontes externas.
- Trate erros de rede e de banco de dados.
- Faça cópias de segurança dos dados importantes.

## 7. Revisão

- O que você aprendeu?
- Que parte ainda parece difícil?
- Consegue explicar o conceito sem olhar o exemplo?
- Consegue modificar o código com segurança?

