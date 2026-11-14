# ============================================================
# DADOS E CONTADORES
# ============================================================

nadadores = []
proximo_id_nadador = 1

historico_movimentacoes = []
proximo_id_movimentacao = 1

TOTAL_TOALHAS = 30
toalhas_disponiveis = TOTAL_TOALHAS

# ============================================================
# TESTE E VALIDAÇÕES
# ============================================================
def validar_nome(nome):
    if not nome.replace(" ","").isalpha():
        return None

def validando_numero(number):
    try:
        # Tenta converter a string em inteiro
        number = int(number)
        
        # Verifica se é positivo (conforme sua mensagem de erro indicava)
        if 0 >= number:
            print("Erro: Digite um número inteiro positivo\n")
            return None
            
        return number
    except ValueError:
        print("Erro: Digite um número inteiro válido\n")
        return None



# ============================================================
# GERENCIAMENTO DE NADADORES
# ============================================================

def buscar_nadador_por_codigo(codigo):
    """Retorna o dicionário do nadador ou None se não existir."""
    for nadador in nadadores:
        if nadador['codigo'] == codigo:
            return nadador
    return None

def listar_nadadores():
    return nadadores

def buscar_nadador_por_nome(consultar_nome):
    """Retorna a lista de nadadores cujo nome contém o texto buscado (lista vazia se nenhum)."""
    lista = [n for n in nadadores if consultar_nome in n['nome'].lower()]
    return lista

def cadastro_nadador(nome):
    global proximo_id_nadador

    if not nome:
        return None

    codigo = proximo_id_nadador
    proximo_id_nadador += 1
    nadadores.append({'codigo': codigo, 'nome': nome, 'toalha': 0})
    return codigo

def retirar_toalhas(nadador, quantidade, toalhas_disponiveis):
    """Tenta retirar toalhas para o nadador.
    Retorna (sucesso, toalhas_disponiveis_atualizado)."""
    if quantidade > toalhas_disponiveis:
        return False, toalhas_disponiveis

    nadador['toalha'] += quantidade
    return True, toalhas_disponiveis - quantidade


def devolver_toalhas(nadador, quantidade, toalhas_disponiveis):
    """Tenta devolver toalhas do nadador ao estoque.
    Retorna (sucesso, toalhas_disponiveis_atualizado)."""
    if quantidade > nadador['toalha']:
        return False, toalhas_disponiveis

    nadador['toalha'] -= quantidade
    return True, toalhas_disponiveis + quantidade


def filtrar_nadadores_com_toalhas():
    """Retorna a lista de nadadores que estão com toalhas."""
    return [n for n in nadadores if n['toalha'] > 0]


# ============================================================
# GERENCIAMENTO DE MOVIMENTAÇÕES
# ============================================================

def listar_movimentacoes():
    return historico_movimentacoes

def registrar_movimentacao(nadador, quantidade, acao):
    """Adiciona uma retirada ou devolução ao histórico."""
    global proximo_id_movimentacao

    historico_movimentacoes.append({
        'ordem': proximo_id_movimentacao,
        'codigo': nadador['codigo'],
        'nome': nadador['nome'],
        'toalha': quantidade,
        'acao': acao,
    })

    proximo_id_movimentacao += 1


def filtrar_movimentacoes_por_codigo(codigo):
    """Retorna os registros do nadador, cada um com sua chave 'ordem'."""
    return [
        item
        for item in historico_movimentacoes
        if item['codigo'] == codigo
    ]


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def solicitar_opcao_menu():
    """Lê a opção do menu. Retorna -1 se não for um número inteiro positivo."""
    opcao = input("\nEscolha uma opção: ").strip()

    if not opcao.isdecimal():
        return -1
    return int(opcao)


def solicitar_codigo():
    """Lê o código do nadador. Retorna None (com mensagem) se for inválido."""
    codigo = input("Código: ").strip()
    # Validando se é um número
    codigo = validando_numero(codigo)
    if codigo is None:
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


def opcao_invalida():
    print("Opção inválida. Por favor, selecione um número do submenu.\n")


def cabecalho(mensagem):
    print(mensagem)


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


def imprimir_movimentacao(item):
    print(f"{item['ordem']:<7}{item['codigo']:<8}{item['nome']:<21}{item['acao']:<15}{item['toalha']:>10}")


# ============================================================
# MENU DE NADADORES
# ============================================================

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
            cabecalho("\n===== CADASTRO DE NADADOR =====\n")
            nome = input("Nome: ").strip().title()
            nome = validar_nome(nome)
            if nome is None:
                print("Erro: O nome não pode ter caracteres especiais ou números")
                return -1

            codigo = cadastro_nadador(nome)

            if codigo is None:
                print("Dados inválidos! O nome não pode ser vazio.\n")
            else:
                print(f"\nNadador cadastrado com sucesso! Código: {codigo}\n")

        elif opcao == 2:
            print(f"\n{' NADADORES '.center(51, '=')}\n")

            lista = listar_nadadores()

            if lista:
                    imprimir_tabela_nadadores(lista) 
            else:
                print("Nenhum nadador cadastrado.\n")

        elif opcao == 3:
            cabecalho("\n===== CONSULTAR NADADOR =====\n")
            codigo = solicitar_codigo()
            if codigo is None:
                continue

            nadador = buscar_nadador_por_codigo(codigo)
            
            if nadador:
                print("\nNadador encontrado:\n")
                imprimir_tabela_nadadores([nadador])
            else:
                print("\nNadador não encontrado.\n")

        elif opcao == 4:
            cabecalho("\n===== PESQUISAR NADADOR =====\n")
            consultar_nome = input("Digite o nome ou parte do nome: ").strip().lower()
            print("")

            lista = buscar_nadador_por_nome(consultar_nome)
            if lista:
                imprimir_tabela_nadadores(lista)
            else:
                print("\nNenhum nadador encontrado.\n")

        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            break
        else:
            opcao_invalida()


# ============================================================
# MENU DE TOALHAS
# ============================================================

def menu_toalhas(toalhas_disponiveis):
    while True:
        print("\n=========== TOALHAS ===========\n")
        print("1 - Retirar toalhas")
        print("2 - Devolver toalhas")
        print("3 - Consultar toalhas em uso")
        print("4 - Consultar toalhas disponíveis")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            cabecalho("\n===== RETIRADA DE TOALHAS =====\n")

            codigo = solicitar_codigo()
            if codigo is None:
                continue

            nadador = buscar_nadador_por_codigo(codigo)
            if nadador is None:
                print(f"Código '{codigo}' não encontrado!\n")
                continue

            quantidade = solicitar_quantidade("Quantidade de toalhas a retirar: ")
            if quantidade is None:
                continue

            sucesso, toalhas_disponiveis = retirar_toalhas(nadador, quantidade, toalhas_disponiveis)

            if sucesso:
                print("\nRetirada registrada com sucesso!")
                print(f"Retirada de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")

                registrar_movimentacao(nadador, quantidade, "Retirada")
            else:
                print(f"\nEstoque insuficiente para {quantidade} toalha(s).")

            print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")

        elif opcao == 2:
            cabecalho("\n===== DEVOLUÇÃO DE TOALHAS =====\n")

            codigo = solicitar_codigo()
            if codigo is None:
                continue

            nadador = buscar_nadador_por_codigo(codigo)
            if nadador is None:
                print(f"Código '{codigo}' não encontrado!\n")
                continue

            if nadador['toalha'] == 0:
                print(f"O nadador {nadador['nome']} (Código: {codigo}) não possui toalhas para devolver.\n")
                continue

            quantidade = solicitar_quantidade(
                f"Nadador possui {nadador['toalha']} toalha(s). Quantas deseja devolver? "
            )
            if quantidade is None:
                continue

            sucesso, toalhas_disponiveis = devolver_toalhas(nadador, quantidade, toalhas_disponiveis)

            if sucesso:
                print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
                print("Devolução registrada com sucesso! Movimentação concluída.\n")

                registrar_movimentacao(nadador, quantidade, "Devolução")
            else:
                print(f"Erro: O nadador {nadador['nome']} possui apenas {nadador['toalha']} toalha(s).\n")

        elif opcao == 3:
            print("\n" + " TOALHAS EM USO ".center(51, '=') + "\n")
            com_toalhas = filtrar_nadadores_com_toalhas()

            if com_toalhas:
                imprimir_tabela_nadadores(com_toalhas)
                print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
            else:
                print("Nenhum nadador está com toalhas no momento.\n")

        elif opcao == 4:
            print("\n" + " ESTOQUE DE TOALHAS ".center(51, '=') + "\n")
            print(f"Toalhas disponíveis: {toalhas_disponiveis} de {TOTAL_TOALHAS}\n")

        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            # Devolve o valor final atualizado para quem chamou o menu_toalhas
            return toalhas_disponiveis

        else:
            opcao_invalida()


# ============================================================
# MENU DE MOVIMENTAÇÕES
# ============================================================

def menu_movimentacoes():
    while True:
        print("\n======== MOVIMENTAÇÕES ========\n")
        print("1 - Consultar movimentações")
        print("2 - Consultar movimentações do nadador")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            cabecalho("\n===== MOVIMENTAÇÕES =====")
            
            lista = listar_movimentacoes()

            if not lista:
                print("\nNenhuma movimentação registrada.\n")
                continue

            imprimir_cabecalho_movimentacoes()
            for item in lista:
                imprimir_movimentacao(item)
            print("")

        elif opcao == 2:
            cabecalho("\n===== MOVIMENTAÇÕES DO NADADOR =====\n")

            codigo = solicitar_codigo()
            if codigo is None:
                continue

            movimentacoes = filtrar_movimentacoes_por_codigo(codigo)

            if not movimentacoes:
                print("\nNenhuma movimentação encontrada para esse código.\n")
                continue

            imprimir_cabecalho_movimentacoes()
            for item in movimentacoes:
                imprimir_movimentacao(item)
            print("")
        
        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            break
        else:
            opcao_invalida()


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu_principal(toalhas_disponiveis):
    while True:
        print('=' * 33)
        print(f"{'NADO LIVRE':^33}")
        print('=' * 33 + "\n")
        print("1 - Nadadores")
        print("2 - Toalhas")
        print("3 - Movimentações")
        print("0 - Sair")
        
        opcao = solicitar_opcao_menu()

        if opcao == 1:
            menu_nadadores()
        elif opcao == 2:
            toalhas_disponiveis = menu_toalhas(toalhas_disponiveis)
        elif opcao == 3:
            menu_movimentacoes()
        elif opcao == 0:
            print("Saindo do sistema... Até logo!")
            break
        else:
            opcao_invalida()


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

menu_principal(toalhas_disponiveis)