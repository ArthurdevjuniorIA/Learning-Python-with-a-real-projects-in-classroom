# ============================================================
# ESTUDO DE CASO: Nado Livre — Sistema de Controle de Toalhas
#
# Integrantes:
# 20261041110027 - Andrew
# 20261041110017 - Arthur
# 20261041110009 - Marcus
# ============================================================

nadadores = []
historico_movimentacoes = []
TOTAL_TOALHAS = 30
toalhas_disponiveis = TOTAL_TOALHAS


# ------------------------------------------------------------
# FUNÇÕES AUXILIARES
# ------------------------------------------------------------

def solicitar_opcao_menu():
    """Lê a opção do menu. Retorna -1 se não for um número inteiro positivo."""
    opcao = input("\nEscolha uma opção: ").strip()

    if not opcao.isdecimal():
        return -1
    return int(opcao)


def solicitar_codigo():
    """Lê o código do nadador. Retorna None (com mensagem) se for inválido."""
    codigo = input("Código: ").strip()

    if not codigo.isdecimal():
        print("Código inválido. Digite um número inteiro positivo.\n")
        return None

    codigo = int(codigo)
    if codigo <= 0:
        print("O código deve ser maior que zero.\n")
        return None
    return codigo


def solicitar_quantidade(mensagem):
    """Lê uma quantidade de toalhas. Retorna None (com mensagem) se for inválida."""
    quantidade = input(mensagem).strip()

    if not quantidade.isdecimal():
        print("Quantidade inválida. Digite um número inteiro positivo.\n")
        return None

    quantidade = int(quantidade)
    if quantidade <= 0:
        print("Quantidade inválida. Digite um número maior que zero.\n")
        return None
    return quantidade


def buscar_nadador_por_codigo(codigo):
    """Retorna o dicionário do nadador ou None se não existir."""
    for nadador in nadadores:
        if nadador['codigo'] == codigo:
            return nadador
    return None


def registrar_movimentacao(nadador, quantidade, acao):
    """Adiciona uma retirada ou devolução ao histórico."""
    historico_movimentacoes.append({
        'codigo': nadador['codigo'],
        'nome': nadador['nome'],
        'toalha': quantidade,
        'acao': acao,
    })


def imprimir_tabela_nadadores(lista):
    """Imprime uma tabela de nadadores com colunas alinhadas."""
    print(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
    print('-' * 51)
    for nadador in lista:
        print(f"{nadador['codigo']:<8}{nadador['nome']:<35}{nadador['toalha']:>8}")
    print("")


def imprimir_cabecalho_movimentacoes():
    print(f"\n{'Ordem':<6}{'Código':>8}  {'Nadador':<20}{'Operação':>12}{'Quantidade':>12}")
    print('-' * 60)


def imprimir_movimentacao(ordem, item):
    print(f"{ordem:<6}{item['codigo']:>8}  {item['nome']:<20}{item['acao']:>12}{item['toalha']:>12}")


# ------------------------------------------------------------
# NADADORES
# ------------------------------------------------------------

def cadastro_nadador():
    print("\n===== CADASTRO DE NADADOR =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return

    if buscar_nadador_por_codigo(codigo):
        print("Código já cadastrado! Tente novamente.\n")
        return

    nome = input("Nome: ").strip().title()
    if not nome:
        print("Dados inválidos! O nome não pode ser vazio.\n")
        return

    nadadores.append({'codigo': codigo, 'nome': nome, 'toalha': 0})
    print("Nadador cadastrado com sucesso!\n")


def listar_nadadores():
    print(f"\n{' NADADORES '.center(51, '=')}\n")

    if nadadores:
        imprimir_tabela_nadadores(nadadores)
    else:
        print("Nenhum nadador cadastrado.\n")


def consultar_nadadores():
    print("\n===== CONSULTAR NADADOR =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return

    encontrado = buscar_nadador_por_codigo(codigo)
    if encontrado:
        print("\nNadador encontrado:\n")
        imprimir_tabela_nadadores([encontrado])
    else:
        print("\nNadador não encontrado.\n")


def pesquisar_nadadores():
    print("\n===== PESQUISAR NADADOR =====\n")
    consultar_nome = input("Digite o nome ou parte do nome: ").strip().lower()

    resultados = [n for n in nadadores if consultar_nome in n['nome'].lower()]

    if resultados:
        print("\nNadador encontrado:\n" if len(resultados) == 1 else "\nNadadores encontrados:\n")
        imprimir_tabela_nadadores(resultados)
    else:
        print("\nNenhum nadador encontrado.\n")


def menu_nadadores():
    while True:
        print("\n========== NADADORES ==========\n")
        print("1 - Cadastrar nadador")
        print("2 - Consultar nadadores")
        print("3 - Consultar nadador por código")
        print("4 - Pesquisar nadador por nome")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            cadastro_nadador()
        elif opcao == 2:
            listar_nadadores()
        elif opcao == 3:
            consultar_nadadores()
        elif opcao == 4:
            pesquisar_nadadores()
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Por favor, selecione um número do submenu.\n")


# ------------------------------------------------------------
# TOALHAS
# ------------------------------------------------------------

def submenu_retirada_toalhas():
    global toalhas_disponiveis

    print("\n===== RETIRADA DE TOALHAS =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return

    nadador = buscar_nadador_por_codigo(codigo)
    if nadador is None:
        print(f"Código '{codigo}' não encontrado!\n")
        return

    quantidade = solicitar_quantidade("Quantidade de toalhas a retirar: ")
    if quantidade is None:
        return

    if quantidade > toalhas_disponiveis:
        print(f"\nEstoque insuficiente para {quantidade} toalha(s).")
        print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
        return

    nadador['toalha'] += quantidade
    toalhas_disponiveis -= quantidade
    registrar_movimentacao(nadador, quantidade, "Retirada")

    print("\nRetirada registrada com sucesso!")
    print(f"Retirada de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
    print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")


def submenu_devolucao_toalhas():
    global toalhas_disponiveis

    print("\n===== DEVOLUÇÃO DE TOALHAS =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return

    nadador = buscar_nadador_por_codigo(codigo)
    if nadador is None:
        print(f"Código '{codigo}' não encontrado!\n")
        return

    if nadador['toalha'] == 0:
        print(f"O nadador {nadador['nome']} (Código: {codigo}) não possui toalhas para devolver.\n")
        return

    quantidade = solicitar_quantidade(
        f"Nadador possui {nadador['toalha']} toalha(s). Quantas deseja devolver? "
    )
    if quantidade is None:
        return

    if quantidade > nadador['toalha']:
        print(f"Erro: O nadador {nadador['nome']} possui apenas {nadador['toalha']} toalha(s).\n")
        return

    nadador['toalha'] -= quantidade
    toalhas_disponiveis += quantidade
    registrar_movimentacao(nadador, quantidade, "Devolução")

    print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
    print("Devolução registrada com sucesso! Movimentação concluída.\n")


def toalhas_em_uso():
    print("\n" + " TOALHAS EM USO ".center(51, '=') + "\n")

    com_toalhas = [n for n in nadadores if n['toalha'] > 0]

    if com_toalhas:
        imprimir_tabela_nadadores(com_toalhas)
        print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
    else:
        print("Nenhum nadador está com toalhas no momento.\n")


def consulta_toalhas():
    print("\n" + " ESTOQUE DE TOALHAS ".center(51, '=') + "\n")
    print(f"Toalhas disponíveis: {toalhas_disponiveis} de {TOTAL_TOALHAS}\n")


def menu_toalhas():
    while True:
        print("\n========== TOALHAS ==========\n")
        print("1 - Retirar toalhas")
        print("2 - Devolver toalhas")
        print("3 - Consultar toalhas em uso")
        print("4 - Consultar toalhas disponíveis")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            submenu_retirada_toalhas()
        elif opcao == 2:
            submenu_devolucao_toalhas()
        elif opcao == 3:
            toalhas_em_uso()
        elif opcao == 4:
            consulta_toalhas()
        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            break
        else:
            print("Opção inválida. Por favor, selecione um número do submenu.\n")


# ------------------------------------------------------------
# MOVIMENTAÇÕES
# ------------------------------------------------------------

def consultar_movimentacoes():
    print("\n===== MOVIMENTAÇÕES =====")

    if not historico_movimentacoes:
        print("\nNenhuma movimentação registrada.\n")
        return

    imprimir_cabecalho_movimentacoes()
    for ordem, item in enumerate(historico_movimentacoes, start=1):
        imprimir_movimentacao(ordem, item)
    print("")


def consultar_movimentacoes_nadadores():
    print("\n===== MOVIMENTAÇÕES DO NADADOR =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return

    # Mantém a ordem original de cada movimentação no histórico geral
    movimentacoes = [
        (ordem, item)
        for ordem, item in enumerate(historico_movimentacoes, start=1)
        if item['codigo'] == codigo
    ]

    if not movimentacoes:
        print("\nNenhuma movimentação encontrada para esse código.\n")
        return

    imprimir_cabecalho_movimentacoes()
    for ordem, item in movimentacoes:
        imprimir_movimentacao(ordem, item)
    print("")


def menu_movimentacoes():
    while True:
        print("\n======== MOVIMENTAÇÕES ========\n")
        print("1 - Consultar movimentações")
        print("2 - Consultar movimentações do nadador")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            consultar_movimentacoes()
        elif opcao == 2:
            consultar_movimentacoes_nadadores()
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Por favor, selecione um número do submenu.\n")


# ------------------------------------------------------------
# MENU PRINCIPAL
# ------------------------------------------------------------

def exibir_menu_principal():
    print('=' * 33)
    print(f"{'NADO LIVRE':^33}")
    print('=' * 33 + "\n")
    print("1 - Nadadores")
    print("2 - Toalhas")
    print("3 - Movimentações")
    print("0 - Sair")


def main():
    while True:
        exibir_menu_principal()

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            menu_nadadores()
        elif opcao == 2:
            menu_toalhas()
        elif opcao == 3:
            menu_movimentacoes()
        elif opcao == 0:
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Por favor, selecione um número do menu.\n")


if __name__ == "__main__":
    main()