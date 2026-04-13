# 🏦 Sistema Bancário em Python

Projeto desenvolvido em Python com o objetivo de praticar **lógica de programação**, **estruturas de controle** e **simulação de operações bancárias**.

---

## 📌 Descrição

Este projeto simula um sistema bancário simples via terminal, permitindo ao usuário realizar operações como:

* Depósito
* Saque (com regras)
* Consulta de saldo
* Visualização de extrato

O sistema funciona em loop contínuo até o usuário escolher sair.

---

## ⚙️ Funcionalidades

* ✔️ Depósito de valores
* ✔️ Saque com limite de R$500 por operação
* ✔️ Limite de até 3 saques diários
* ✔️ Consulta de saldo em tempo real
* ✔️ Exibição de extrato (depósitos e saques)
* ✔️ Validação de valores inválidos
* ✔️ Interface simples via terminal

---

## 🧠 Conceitos aplicados

* Estruturas condicionais (`if`, `elif`, `else`)
* Estrutura de repetição (`while`)
* Listas (`list`) para controle de extrato
* Variáveis acumuladoras
* Controle de fluxo
* Entrada de dados com `input()`
* Uso da biblioteca `time` (`sleep`)

---

## ▶️ Como executar

1. Certifique-se de ter o Python instalado (versão 3.x)

2. Clone este repositório:

```bash
git clone https://github.com/Yurizin3333/Sistema-Bancario
```

3. Acesse a pasta do projeto:

```bash
cd Sistema-Bancario
```

4. Execute o arquivo:

```bash
python sistema_bancario.py
```

---

## 💻 Exemplo de uso

```bash
=============MENU BANCO=============

[ 1 ] Deposito
[ 2 ] Saque
[ 3 ] Saldo
[ 4 ] Extrato
[ 5 ] Sair

>>>>Sua Resposta: 1

>>>Quanto Você Quer Depositar?: 100
+++++++++++++++R$100 Depositado Com Sucesso!+++++++++++++++

>>>>Sua Resposta: 2

>>>Qual Valor Você Quer Sacar?[Max=500]: 50
+++++++++++++++R$50 Sacados com Sucesso!+++++++++++++++

>>>>Sua Resposta: 3
<<<Seu saldo atual é de R$50...

>>>>Sua Resposta: 4
<<Depositos Feitos: [100.0]
>>Saques Feitos: [50.0]
```

---

## 📁 Estrutura do projeto

```
Sistema-Bancario/
│
├── sistema_bancario.py
└── README.md
```

---

## 🚀 Melhorias futuras

* Adicionar autenticação de usuário (login/senha)
* Armazenar dados em banco de dados (SQLite/MySQL)
* Melhorar formatação do extrato
* Criar interface gráfica (GUI)
* Implementar orientação a objetos (POO)

---

## 👨‍💻 Autor

**Yuri da Silva Ignacio**

* GitHub: https://github.com/Yurizin3333
* LinkedIn: https://www.linkedin.com/in/yuri-d-332701246/

---

## 📄 Licença

Este projeto é de uso livre para fins de estudo e aprendizado.
