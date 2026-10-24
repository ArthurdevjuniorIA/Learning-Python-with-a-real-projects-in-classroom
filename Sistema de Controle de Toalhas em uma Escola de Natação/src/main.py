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


def buscar_nadador_por_codigo(codigo, nadadores):
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


def cabecalho_da_tabela(texto):
    print(texto)
    print('-' * 61)

def imprimir_tabela_nadadores(lista):
    """Imprime uma tabela de nadadores com colunas alinhadas."""
    cabecalho_da_tabela(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
    
    for nadador in lista:
        print(f"{nadador['codigo']:<8}{nadador['nome']:<35}{nadador['toalha']:>8}")
    print("")


def imprimir_cabecalho_movimentacoes():


    cabecalho_da_tabela(f"\n{'Ordem':<7}{'Código':<8}{'Nadador':<21}{'Operação':<15}{'Quantidade':>10}")


def imprimir_movimentacao(ordem, item):
    cabecalho_da_tabela(f"{ordem:<7}{item['codigo']:<8}{item['nome']:<21}{item['acao']:<15}{item['toalha']:>10}")

# ------------------------------------------------------------
# NADADORES
# ------------------------------------------------------------

def cadastro_nadador(nadadores):
    print("\n===== CADASTRO DE NADADOR =====\n")

    codigo = solicitar_codigo()
    if codigo is None:

        return 

    if buscar_nadador_por_codigo(codigo, nadadores):
        print("Código já cadastrado! Tente novamente.\n")
        return

    nome = input("Nome: ").strip().title()
    if not nome:
        print("Dados inválidos! O nome não pode ser vazio.\n")
        return

    nadadores.append({'codigo': codigo, 'nome': nome, 'toalha': 0})
    print("Nadador cadastrado com sucesso!\n")


def listar_nadadores(nadadores):
    print(f"\n{' NADADORES '.center(51, '=')}\n")

    if nadadores:
        imprimir_tabela_nadadores(nadadores)
    else:
        print("Nenhum nadador cadastrado.\n")


def consultar_nadadores(nadadores):
    print("\n===== CONSULTAR NADADOR =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return 

    encontrado = buscar_nadador_por_codigo(codigo, nadadores)
    if encontrado:
        print("\nNadador encontrado:\n")
        imprimir_tabela_nadadores([encontrado])
    else:
        print("\nNadador não encontrado.\n")


def pesquisar_nadadores(nadadores):
    print("\n===== PESQUISAR NADADOR =====\n")
    consultar_nome = input("Digite o nome ou parte do nome: ").strip().lower()

    resultados = [n for n in nadadores if consultar_nome in n['nome'].lower()]

    if resultados:
        print("\nNadador encontrado:\n" if len(resultados) == 1 else "\nNadadores encontrados:\n")
        imprimir_tabela_nadadores(resultados)
    else:
        print("\nNenhum nadador encontrado.\n")

def exibir_menu_nadadores():
    print("\n========== NADADORES ==========\n")
    print("1 - Cadastrar nadador")
    print("2 - Consultar nadadores")
    print("3 - Consultar nadador por código")
    print("4 - Pesquisar nadador por nome")
    print("0 - Voltar")

def menu_nadadores(nadadores):
    while True:
        exibir_menu_nadadores()

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            cadastro_nadador(nadadores)
        elif opcao == 2:
            listar_nadadores(nadadores)
        elif opcao == 3:
            consultar_nadadores(nadadores)
        elif opcao == 4:
            pesquisar_nadadores(nadadores)
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Por favor, selecione um número do submenu.\n")


# ------------------------------------------------------------
# TOALHAS
# ------------------------------------------------------------

def submenu_retirada_toalhas(toalhas_em_uso, nadadores):

    print("\n===== RETIRADA DE TOALHAS =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return toalhas_em_uso

    nadador = buscar_nadador_por_codigo(codigo, nadadores)
    if nadador is None:
        print(f"Código '{codigo}' não encontrado!\n")
        return toalhas_em_uso

    quantidade = solicitar_quantidade("Quantidade de toalhas a retirar: ")
    if quantidade is None:
        return toalhas_em_uso

    quantidade = int(quantidade)
    if quantidade > toalhas_em_uso:
        print(f"\nEstoque insuficiente para {quantidade} toalha(s).")
        print(f"Toalhas disponíveis: {toalhas_em_uso}\n")
        return toalhas_em_uso

    nadador['toalha'] += quantidade
    toalhas_em_uso -= quantidade
    registrar_movimentacao(nadador, quantidade, "Retirada")

    print("\nRetirada registrada com sucesso!")
    print(f"Retirada de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
    print(f"Toalhas disponíveis no estoque: {toalhas_em_uso}\n")
    return toalhas_em_uso

def submenu_devolucao_toalhas(toalhas_em_uso, nadadores):

    print("\n===== DEVOLUÇÃO DE TOALHAS =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return toalhas_em_uso

    nadador = buscar_nadador_por_codigo(codigo, nadadores)
    if nadador is None:
        print(f"Código '{codigo}' não encontrado!\n")
        return toalhas_em_uso

    if nadador['toalha'] == 0:
        print(f"O nadador {nadador['nome']} (Código: {codigo}) não possui toalhas para devolver.\n")
        return toalhas_em_uso

    quantidade = solicitar_quantidade(
        f"Nadador possui {nadador['toalha']} toalha(s). Quantas deseja devolver? "
    )
    if quantidade is None:
        return toalhas_em_uso

    if quantidade > nadador['toalha']:
        print(f"Erro: O nadador {nadador['nome']} possui apenas {nadador['toalha']} toalha(s).\n")
        return toalhas_em_uso

    nadador['toalha'] -= quantidade
    toalhas_em_uso += quantidade
    registrar_movimentacao(nadador, quantidade, "Devolução")

    print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
    print("Devolução registrada com sucesso! Movimentação concluída.\n")
    return toalhas_em_uso

def listar_toalhas_em_uso(toalhas_em_uso):
    print("\n" + " TOALHAS EM USO ".center(51, '=') + "\n")

    com_toalhas = [n for n in nadadores if n['toalha'] > 0]

    if com_toalhas:
        imprimir_tabela_nadadores(com_toalhas)
        print(f"Toalhas disponíveis no estoque: {toalhas_em_uso}\n")
    else:
        print("Nenhum nadador está com toalhas no momento.\n")
    return toalhas_em_uso

def exibir_menu_toalhas():
    print("\n=========== TOALHAS ===========\n")
    print("1 - Retirar toalhas")
    print("2 - Devolver toalhas")
    print("3 - Consultar toalhas em uso")
    print("4 - Consultar toalhas disponíveis")
    print("0 - Voltar")

    
def menu_toalhas(toalhas_em_uso):
    while True:
        exibir_menu_toalhas()
       
        opcao = solicitar_opcao_menu()

        if opcao == 1:
             # Armazena o restante das toalhas na variável toalhas em uso
            toalhas_em_uso = submenu_retirada_toalhas(toalhas_em_uso, nadadores)

        elif opcao == 2:
            # Armazena o restante das toalhas na variável toalhas em uso
            toalhas_em_uso = submenu_devolucao_toalhas(toalhas_em_uso, nadadores)

        elif opcao == 3:
            # Chama a função que lista os nadadores com toalha
            listar_toalhas_em_uso(toalhas_em_uso)

        elif opcao == 4:
            # Imprime a consulta na tela
            print("\n" + " ESTOQUE DE TOALHAS ".center(51, '=') + "\n")
            print(f"Toalhas disponíveis: {toalhas_em_uso} de {TOTAL_TOALHAS}\n")

        elif opcao == 0:
            # Retorna o valor final atualizado para quem chamou o menu_toalhas
            return toalhas_em_uso
        
        else:
            print("Opção inválida. Por favor, selecione um número do submenu.\n")
    

# ------------------------------------------------------------
# MOVIMENTAÇÕES
# ------------------------------------------------------------

def consultar_movimentacoes(historico_movimentacoes):
    print("\n===== MOVIMENTAÇÕES =====")

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


def consultar_movimentacoes_nadadores(historico_movimentacoes):
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

def exibir_menu_movimentacoes():
    print("\n======== MOVIMENTAÇÕES ========\n")
    print("1 - Consultar movimentações")
    print("2 - Consultar movimentações do nadador")
    print("0 - Voltar")


def menu_movimentacoes(historico_movimentacoes):
    while True:
        exibir_menu_movimentacoes()

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            consultar_movimentacoes(historico_movimentacoes)
        elif opcao == 2:
            consultar_movimentacoes_nadadores(historico_movimentacoes)
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

# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

while True:
    exibir_menu_principal()

    opcao = solicitar_opcao_menu()

    if opcao == 1:
        menu_nadadores(nadadores)
    elif opcao == 2:
        toalhas_disponiveis = menu_toalhas(toalhas_disponiveis)
    elif opcao == 3:
        menu_movimentacoes(historico_movimentacoes)
    elif opcao == 0:
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida. Por favor, selecione um número do menu.\n")