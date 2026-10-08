# Nado Livre: Sistema de Controle de Toalhas

Estudo de Caso desenvolvido em Python para o controle de empréstimo de toalhas em um clube de natação.

## Integrantes

| Matrícula       | Nome   |
|-----------------|--------|
| 20261041110027  | Andrew |
| 20261041110017  | Arthur |
| 20261041110009  | Marcus |

## Descrição do sistema

O **Nado Livre** é um programa executado no terminal que controla o empréstimo de toalhas para os nadadores. O estoque inicial é de **30 toalhas**.

Com ele é possível:

- cadastrar nadadores e consultá-los por código ou por nome;
- registrar a retirada e a devolução de toalhas, validando o estoque e a quantidade que cada nadador possui;
- consultar as toalhas em uso e o estoque disponível;
- consultar o histórico de movimentações, geral ou por nadador.

Os dados ficam em memória (listas e dicionários) e a navegação é feita por menus e submenus.

## Como executar
```bash
cd Sistema de controle de Toalhas em uma escola de natação
```
```bash
python main.py
```

Requer Python 3.6 ou superior (uso de f-strings).

## Estrutura de menus

```
NADO LIVRE
├── 1 - Nadadores
│   ├── 1 - Cadastrar nadador
│   ├── 2 - Consultar nadadores
│   ├── 3 - Consultar nadador por código
│   └── 4 - Pesquisar nadador por nome
├── 2 - Toalhas
│   ├── 1 - Retirar toalhas
│   ├── 2 - Devolver toalhas
│   ├── 3 - Consultar toalhas em uso
│   └── 4 - Consultar toalhas disponíveis
├── 3 - Movimentações
│   ├── 1 - Consultar movimentações
│   └── 2 - Consultar movimentações do nadador
└── 0 - Sair
```

## Principais funções

| Função | Responsabilidade |
|--------|------------------|
| `menu_principal()` | Exibe o menu inicial e direciona para cada submenu. |
| `menu_nadadores()` | Submenu de nadadores; chama as funções de cadastro, listagem e busca. |
| `cadastrar_nadador()` | Cadastra um nadador, validando código numérico, positivo e único, e nome não vazio. |
| `listar_nadadores()` | Lista todos os nadadores cadastrados. |
| `consultar_nadador_por_codigo()` | Busca um nadador pelo código. |
| `pesquisar_nadador_por_nome()` | Busca nadadores pelo nome ou parte dele. |
| `menu_toalhas()` | Submenu de toalhas: retirada, devolução, toalhas em uso e estoque. Atualiza `toalhas_disponiveis` e registra cada operação no histórico. |
| `menu_movimentacoes()` | Consulta o histórico completo ou apenas as movimentações de um nadador. |

## Refatoração

O código foi dividido por responsabilidade: uma função para o menu principal e uma para cada área do sistema (nadadores, toalhas e movimentações), em vez de um único bloco com vários `if/elif` aninhados.

### Como a refatoração melhorou a organização

- **Legibilidade:** cada função tem um propósito claro e o menu principal funciona apenas como roteador.
- **Manutenção:** um problema no cadastro, por exemplo, é procurado só nas funções de nadadores, sem afetar o restante.
- **Dados centralizados:** as variáveis compartilhadas ficam no topo do arquivo e são usadas por todos os menus.
- **Facilidade para evoluir:** novas opções entram no submenu correto sem mexer nos demais.

### Correções aplicadas na revisão

| # | Problema | Correção |
|---|----------|----------|
| 1 | `continue` dentro de função aninhada gerava `SyntaxError` e impedia o programa de rodar. | Substituído por `return`. |
| 2 | `cod_input` indefinido no cadastro quando o usuário digitava letras (`NameError`). | Adicionado `return` no `except`. |
| 3 | Funções `opcao_N_...` eram redefinidas a cada volta do `while`. | Movidas para o nível do módulo. |
| 4 | Nomes inconsistentes (`Menu` / `menu`). | Padronizados em `snake_case` com nomes descritivos. |
| 5 | Códigos zero ou negativos eram aceitos. | Validação de código maior que zero. |
| 6 | Tabelas desalinhadas (cabeçalho e linhas com larguras diferentes). | Mesmas larguras de coluna no cabeçalho e nas linhas. |
| 7 | Consultas de movimentações sem aviso quando não havia resultados. | Mensagem "Nenhuma movimentação encontrada." |
| 8 | "Toalhas em uso" dependia apenas do estoque. | Verifica se algum nadador possui `toalha > 0`. |
| 9 | `encontrado = False` recebendo um dicionário. | Uso de `None`. |
