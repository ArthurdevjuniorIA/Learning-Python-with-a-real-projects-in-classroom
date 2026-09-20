# 🏊‍♂️ Nado Livre — Sistema de Controle de Toalhas

O **Nado Livre** é um sistema em Python desenvolvido para gerenciamento de nadadores e controle do fluxo de empréstimo e devolução de toalhas de uma academia/clube de natação. O sistema garante o rastreamento preciso do estoque de toalhas, histórico de movimentações e prevenção de erros operacionais.

---

## 👥 Integrantes do Projeto

* **Andrew Rafael**
* **Arthur Kauã** 
* **Marcus Paulo** 

---

## 🎯 Funcionalidades

### 1. 👤 Gestão de Nadadores
* **Cadastrar Nadador:** Registo com código único e formatação automática de nome.
* **Consultar Nadadores:** Listagem geral formatada em tabela de todos os nadadores cadastrados.
* **Consultar por Código:** Busca rápida e direta utilizando o código único do atleta.
* **Pesquisar por Nome:** Busca flexível por nome completo ou partes do nome (case-insensitive).

### 2. 🧺 Controle de Toalhas
* **Retirar Toalhas:** Empréstimo com validação de estoque e verificação de cadastro do nadador.
* **Devolver Toalhas:** Processamento de devolução com validações contra devoluções excedentes ou para nadadores sem toalhas pendentes.
* **Toalhas em Uso:** Relatório detalhado exibindo quem está em posse de toalhas no momento.
* **Estoque de Toalhas:** Painel em tempo real da quantidade de toalhas disponíveis versus capacidade total ($30$ unidades).

### 3. 📜 Registros e Movimentações
* **Histórico Geral:** Registro em ordem cronológica de todas as retiradas e devoluções executadas no sistema.
* **Histórico Individual:** Filtragem das movimentações por código do nadador.

---

## 💡 Decisões de Design e UX

* **Submenus Persistentes:** O sistema mantém o utilizador no submenu atual após cada operação concluída, evitando navegações redundantes até que seja acionada a opção `0 - Voltar`.
* **Identificador Único:** O código do nadador é tratado como chave primária única, garantindo a integridade nas buscas e nos históricos de movimentação.
* **Tratamento de Exceções:** Todos os dados de entrada (`inputs`) possuem validações com blocos `try/except` para impedir falhas de execução por dados mal formatados ou tipos inválidos.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** [Python 3.x](https://www.python.org/)
* **Estrutura de Dados:** Listas e Dicionários nativos para armazenamento em memória.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Ter o Python 3 instalado no seu computador.

### Passo a Passo

1. **Clone ou baixe o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nado-livre.git](https://github.com/seu-usuario/nado-livre.git)
2. **Acesse a pasta do projeto**
```bash 
  cd nado-livre
````
3. **Execute o arquivo principal**
```bash
  python main.py
````
