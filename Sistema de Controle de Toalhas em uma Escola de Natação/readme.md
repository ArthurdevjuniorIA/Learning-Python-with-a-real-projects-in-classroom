# 🏊 Nado Livre — Sistema de Controle de Toalhas

Sistema de linha de comando, desenvolvido em **Python**, para gerenciar o empréstimo de toalhas em uma academia de natação. Ele permite cadastrar nadadores, controlar retiradas e devoluções e consultar o histórico completo de movimentações, mantendo o estoque sempre atualizado.

> Projeto acadêmico desenvolvido em equipe como estudo de caso. Faz parte do repositório [Learning Python with real projects in classroom](../README.md).

---

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Como executar](#-como-executar)
- [Estrutura de menus](#-estrutura-de-menus)
- [Regras de negócio](#-regras-de-negócio)
- [Validações de entrada](#-validações-de-entrada)
- [Estrutura de dados](#-estrutura-de-dados)
- [Exemplo de uso](#-exemplo-de-uso)
- [Possíveis melhorias](#-possíveis-melhorias)
- [Integrantes](#-integrantes)

---

## ✨ Funcionalidades

**Nadadores**
- Cadastrar nadador (código único + nome)
- Listar todos os nadadores
- Consultar nadador por código
- Pesquisar nadador por nome (busca parcial, sem diferenciar maiúsculas/minúsculas)

**Toalhas**
- Retirar toalhas
- Devolver toalhas
- Consultar quais nadadores estão com toalhas em uso
- Consultar a quantidade de toalhas disponíveis no estoque

**Movimentações**
- Consultar o histórico geral de retiradas e devoluções
- Consultar o histórico de um nadador específico (mantendo a ordem original do histórico geral)

---

## 🛠 Tecnologias

- [Python 3.6+](https://www.python.org/) (utiliza f-strings)
- Apenas a biblioteca padrão — **nenhuma dependência externa**

---

## 🚀 Como executar

**1. Clone o repositório e entre na pasta do projeto**

```bash
git clone https://github.com/ArthurdevjuniorIA/Learning-Python-with-a-real-projects-in-classroom.git
cd Learning-Python-with-a-real-projects-in-classroom/"Sistema de Controle de Toalhas"
```

**2. Execute o programa**

```bash
python main.py
```

> Em alguns sistemas (Linux/macOS), pode ser necessário usar `python3 main.py`.
> Ajuste o nome do arquivo caso o seu seja diferente de `main.py`.

---

## 🧭 Estrutura de menus

```
NADO LIVRE
├── 1 - Nadadores
│   ├── 1 - Cadastrar nadador
│   ├── 2 - Consultar nadadores
│   ├── 3 - Consultar nadador por código
│   ├── 4 - Pesquisar nadador por nome
│   └── 0 - Voltar
├── 2 - Toalhas
│   ├── 1 - Retirar toalhas
│   ├── 2 - Devolver toalhas
│   ├── 3 - Consultar toalhas em uso
│   ├── 4 - Consultar toalhas disponíveis
│   └── 0 - Voltar
├── 3 - Movimentações
│   ├── 1 - Consultar movimentações
│   ├── 2 - Consultar movimentações do nadador
│   └── 0 - Voltar
└── 0 - Sair
```

---

## 📏 Regras de negócio

- O estoque inicial é de **30 toalhas** (constante `TOTAL_TOALHAS`).
- Cada nadador possui um **código único** (inteiro positivo).
- Só é possível retirar toalhas de nadadores **previamente cadastrados**.
- Uma retirada **não pode exceder** o estoque disponível.
- Uma devolução **não pode exceder** a quantidade de toalhas que o nadador possui.
- Nadadores sem toalhas não podem realizar devolução.
- Toda retirada e devolução é registrada no histórico, com código, nome, quantidade e tipo de operação.
- Os nomes são padronizados automaticamente (ex.: `maria silva` → `Maria Silva`).

---

## ✅ Validações de entrada

| Entrada | Validação |
|---|---|
| Opção de menu | Deve ser um número inteiro; caso contrário, exibe "Opção inválida" |
| Código | Deve ser inteiro positivo (maior que zero) |
| Quantidade | Deve ser inteiro positivo (maior que zero) |
| Nome | Não pode ser vazio |
| Código duplicado | Não permite cadastrar dois nadadores com o mesmo código |

---

## 🗂 Estrutura de dados

Os dados são mantidos **em memória** durante a execução, usando listas de dicionários.

**Nadador**
```python
{'codigo': 1, 'nome': 'Maria Silva', 'toalha': 2}
```

**Movimentação**
```python
{'codigo': 1, 'nome': 'Maria Silva', 'toalha': 2, 'acao': 'Retirada'}
```

> ⚠️ Como não há persistência em arquivo ou banco de dados, **todos os dados são perdidos ao encerrar o programa**.

---

## 💻 Exemplo de uso

```text
=================================
           NADO LIVRE
=================================

1 - Nadadores
2 - Toalhas
3 - Movimentações
0 - Sair

Escolha uma opção: 2

========== TOALHAS ==========

1 - Retirar toalhas
...
Escolha uma opção: 1

===== RETIRADA DE TOALHAS =====

Código: 1
Quantidade de toalhas a retirar: 2

Retirada registrada com sucesso!
Retirada de 2 toalha(s) pelo nadador Maria Silva (Código: 1)
Toalhas disponíveis no estoque: 28
```

**Histórico de movimentações**

```text
Ordem   Código  Nadador                Operação  Quantidade
------------------------------------------------------------
1            1  Maria Silva            Retirada           2
2            1  Maria Silva           Devolução           1
```

---

## 🔮 Possíveis melhorias

- Persistência dos dados (arquivo JSON/CSV ou banco de dados SQLite)
- Registro de data e hora em cada movimentação
- Remoção e edição de nadadores cadastrados
- Relatórios (nadadores com mais retiradas, toalhas em atraso etc.)
- Testes automatizados com `unittest` ou `pytest`
- Interface gráfica ou versão web

---

## 👥 Integrantes

| Matrícula | Nome |
|---|---|
| 202610411100** | Andrew |
| 202610411100** | Arthur |
| 202610411100** | Marcus |

---

## 📄 Licença

Projeto desenvolvido para fins educacionais.
