# ============================================================
# DADOS E CONTADORES
# ============================================================

# Lista de nadadores: {"id", "nome"}
nadadores = []
proximo_id_nadador = 1

# Lista de movimentações: {"id", "nadador_id", "quantidade", "acao"}
movimentacoes = []
proximo_id_movimentacao = 1

# Constantes (não são alteradas durante a execução)
TOTAL_TOALHAS = 30
ACAO_RETIRADA = "Retirada"
ACAO_DEVOLUCAO = "Devolução"

# O saldo de cada nadador e o estoque NÃO são armazenados:
# são calculados a partir das movimentações, evitando dados duplicados.


# ============================================================
# GERENCIAMENTO DE NADADORES
# ============================================================

def inserir_nadador(nome):
    """Cadastra um nadador. Retorna o registro criado ou None se o nome for vazio."""
    global proximo_id_nadador

    if not nome:
        return None

    nadador = {
        "id": proximo_id_nadador,
        "nome": nome
    }

    nadadores.append(nadador)
    proximo_id_nadador += 1

    return nadador


def listar_nadadores():
    return nadadores


def consultar_nadador(id_nadador):
    """Retorna o nadador com o id informado ou None se não existir."""
    for nadador in nadadores:
        if nadador["id"] == id_nadador:
            return nadador

    return None


def nadadores_por_nome(nome):
    """Retorna os nadadores cujo nome contém o texto (sem diferenciar maiúsculas)."""
    resultado = []

    for nadador in nadadores:
        if nome.lower() in nadador["nome"].lower():
            resultado.append(nadador)

    return resultado


def alterar_nadador(id_nadador, nome):
    """Altera o nome do nadador. Retorna (sucesso, mensagem_de_erro)."""
    nadador = consultar_nadador(id_nadador)

    if nadador is None:
        return False, "Nadador não encontrado."
    if not nome:
        return False, "O nome não pode ser vazio."

    nadador["nome"] = nome
    return True, ""


def remover_nadador(id_nadador):
    """Remove o nadador. Retorna (sucesso, mensagem_de_erro).
    Não permite remover quem está com toalhas ou possui movimentações."""
    nadador = consultar_nadador(id_nadador)

    if nadador is None:
        return False, "Nadador não encontrado."
    if toalhas_do_nadador(id_nadador) > 0:
        return False, "O nadador está com toalhas e deve devolvê-las antes."
    if movimentacoes_por_nadador(id_nadador):
        return False, "O nadador possui movimentações registradas e não pode ser removido."

    nadadores.remove(nadador)
    return True, ""


# ============================================================
# GERENCIAMENTO DE MOVIMENTAÇÕES
# ============================================================

def inserir_movimentacao(id_nadador, quantidade, acao):
    """Registra uma retirada ou devolução.
    Retorna o registro criado ou None se o nadador não existir."""
    global proximo_id_movimentacao

    if consultar_nadador(id_nadador) is None:
        return None

    movimentacao = {
        "id": proximo_id_movimentacao,
        "nadador_id": id_nadador,
        "quantidade": quantidade,
        "acao": acao
    }

    movimentacoes.append(movimentacao)
    proximo_id_movimentacao += 1

    return movimentacao


def listar_movimentacoes():
    return movimentacoes


def movimentacoes_por_nadador(id_nadador):
    """Retorna as movimentações de um nadador."""
    resultado = []

    for movimentacao in movimentacoes:
        if movimentacao["nadador_id"] == id_nadador:
            resultado.append(movimentacao)

    return resultado


# ============================================================
# GERENCIAMENTO DE TOALHAS (ESTOQUE)
# ============================================================

def toalhas_do_nadador(id_nadador):
    """Retorna quantas toalhas o nadador está usando no momento."""
    saldo = 0

    for movimentacao in movimentacoes_por_nadador(id_nadador):
        if movimentacao["acao"] == ACAO_RETIRADA:
            saldo += movimentacao["quantidade"]
        else:
            saldo -= movimentacao["quantidade"]

    return saldo


def consultar_estoque():
    """Retorna quantas toalhas estão disponíveis."""
    em_uso = 0

    for movimentacao in movimentacoes:
        if movimentacao["acao"] == ACAO_RETIRADA:
            em_uso += movimentacao["quantidade"]
        else:
            em_uso -= movimentacao["quantidade"]

    return TOTAL_TOALHAS - em_uso


def nadadores_com_toalhas():
    """Retorna os nadadores que estão com toalhas no momento."""
    resultado = []

    for nadador in nadadores:
        if toalhas_do_nadador(nadador["id"]) > 0:
            resultado.append(nadador)

    return resultado


def retirar_toalhas(id_nadador, quantidade):
    """Retira toalhas para o nadador e registra a movimentação.
    Retorna (sucesso, mensagem_de_erro)."""
    if consultar_nadador(id_nadador) is None:
        return False, "Nadador não encontrado."
    if quantidade > consultar_estoque():
        return False, f"Estoque insuficiente para {quantidade} toalha(s)."

    inserir_movimentacao(id_nadador, quantidade, ACAO_RETIRADA)
    return True, ""


def devolver_toalhas(id_nadador, quantidade):
    """Devolve toalhas do nadador ao estoque e registra a movimentação.
    Retorna (sucesso, mensagem_de_erro)."""
    nadador = consultar_nadador(id_nadador)

    if nadador is None:
        return False, "Nadador não encontrado."

    em_posse = toalhas_do_nadador(id_nadador)

    if em_posse == 0:
        return False, f"O nadador {nadador['nome']} não possui toalhas para devolver."
    if quantidade > em_posse:
        return False, f"O nadador {nadador['nome']} possui apenas {em_posse} toalha(s)."

    inserir_movimentacao(id_nadador, quantidade, ACAO_DEVOLUCAO)
    return True, ""


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


def opcao_invalida():
    print("Opção inválida. Por favor, selecione um número do submenu.\n")


def cabecalho_da_tabela(texto):
    print(texto)
    print('-' * 61)


def imprimir_tabela_nadadores(lista):
    """Imprime uma tabela de nadadores com colunas alinhadas."""
    cabecalho_da_tabela(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")

    for nadador in lista:
        toalhas = toalhas_do_nadador(nadador['id'])
        print(f"{nadador['id']:<8}{nadador['nome']:<35}{toalhas:>8}")
    print("")


def imprimir_cabecalho_movimentacoes():
    cabecalho_da_tabela(f"\n{'Ordem':<7}{'Código':<8}{'Nadador':<21}{'Operação':<15}{'Quantidade':>10}")


def imprimir_movimentacao(movimentacao):
    nadador = consultar_nadador(movimentacao['nadador_id'])
    nome = nadador['nome'] if nadador else "Não encontrado"

    print(f"{movimentacao['id']:<7}{movimentacao['nadador_id']:<8}{nome:<21.20}"
          f"{movimentacao['acao']:<15}{movimentacao['quantidade']:>10}")


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
        print("5 - Alterar nome do nadador")
        print("6 - Remover nadador")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            print("\n===== CADASTRO DE NADADOR =====\n")
            nome = input("Nome: ").strip().title()
            nadador = inserir_nadador(nome)

            if nadador is None:
                print("Dados inválidos! O nome não pode ser vazio.\n")
            else:
                print(f"\nNadador cadastrado com sucesso! Código: {nadador['id']}\n")

        elif opcao == 2:
            print(f"\n{' NADADORES '.center(51, '=')}\n")

            lista = listar_nadadores()

            if lista:
                imprimir_tabela_nadadores(lista)
            else:
                print("Nenhum nadador cadastrado.\n")

        elif opcao == 3:
            print("\n===== CONSULTAR NADADOR =====\n")
            codigo = solicitar_codigo()
            if codigo is None:
                continue

            nadador = consultar_nadador(codigo)

            if nadador:
                print("\nNadador encontrado:\n")
                imprimir_tabela_nadadores([nadador])
            else:
                print("\nNadador não encontrado.\n")

        elif opcao == 4:
            print("\n===== PESQUISAR NADADOR =====\n")
            texto = input("Digite o nome ou parte do nome: ").strip()
            print("")

            lista = nadadores_por_nome(texto)
            if lista:
                imprimir_tabela_nadadores(lista)
            else:
                print("Nenhum nadador encontrado.\n")

        elif opcao == 5:
            print("\n===== ALTERAR NADADOR =====\n")
            codigo = solicitar_codigo()
            if codigo is None:
                continue

            nome = input("Novo nome: ").strip().title()
            sucesso, erro = alterar_nadador(codigo, nome)

            if sucesso:
                print("\nNadador alterado com sucesso!\n")
            else:
                print(f"\n{erro}\n")

        elif opcao == 6:
            print("\n===== REMOVER NADADOR =====\n")
            codigo = solicitar_codigo()
            if codigo is None:
                continue

            sucesso, erro = remover_nadador(codigo)

            if sucesso:
                print("\nNadador removido com sucesso!\n")
            else:
                print(f"\n{erro}\n")

        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            break
        else:
            opcao_invalida()


# ============================================================
# MENU DE TOALHAS
# ============================================================

def menu_toalhas():
    while True:
        print("\n=========== TOALHAS ===========\n")
        print("1 - Retirar toalhas")
        print("2 - Devolver toalhas")
        print("3 - Consultar toalhas em uso")
        print("4 - Consultar toalhas disponíveis")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            print("\n===== RETIRADA DE TOALHAS =====\n")

            codigo = solicitar_codigo()
            if codigo is None:
                continue

            nadador = consultar_nadador(codigo)
            if nadador is None:
                print(f"Código '{codigo}' não encontrado!\n")
                continue

            quantidade = solicitar_quantidade("Quantidade de toalhas a retirar: ")
            if quantidade is None:
                continue

            sucesso, erro = retirar_toalhas(codigo, quantidade)

            if sucesso:
                print("\nRetirada registrada com sucesso!")
                print(f"Retirada de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
            else:
                print(f"\n{erro}")

            print(f"Toalhas disponíveis no estoque: {consultar_estoque()}\n")

        elif opcao == 2:
            print("\n===== DEVOLUÇÃO DE TOALHAS =====\n")

            codigo = solicitar_codigo()
            if codigo is None:
                continue

            nadador = consultar_nadador(codigo)
            if nadador is None:
                print(f"Código '{codigo}' não encontrado!\n")
                continue

            # Apenas para evitar pedir a quantidade sem necessidade;
            # a validação oficial é feita em devolver_toalhas().
            em_posse = toalhas_do_nadador(codigo)
            if em_posse == 0:
                print(f"O nadador {nadador['nome']} (Código: {codigo}) não possui toalhas para devolver.\n")
                continue

            quantidade = solicitar_quantidade(
                f"Nadador possui {em_posse} toalha(s). Quantas deseja devolver? "
            )
            if quantidade is None:
                continue

            sucesso, erro = devolver_toalhas(codigo, quantidade)

            if sucesso:
                print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
                print("Devolução registrada com sucesso! Movimentação concluída.\n")
            else:
                print(f"Erro: {erro}\n")

        elif opcao == 3:
            print("\n" + " TOALHAS EM USO ".center(51, '=') + "\n")
            com_toalhas = nadadores_com_toalhas()

            if com_toalhas:
                imprimir_tabela_nadadores(com_toalhas)
                print(f"Toalhas disponíveis no estoque: {consultar_estoque()}\n")
            else:
                print("Nenhum nadador está com toalhas no momento.\n")

        elif opcao == 4:
            print("\n" + " ESTOQUE DE TOALHAS ".center(51, '=') + "\n")
            print(f"Toalhas disponíveis: {consultar_estoque()} de {TOTAL_TOALHAS}\n")

        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            break
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
            print("\n===== MOVIMENTAÇÕES =====")

            lista = listar_movimentacoes()

            if not lista:
                print("\nNenhuma movimentação registrada.\n")
                continue

            imprimir_cabecalho_movimentacoes()
            for movimentacao in lista:
                imprimir_movimentacao(movimentacao)
            print("")

        elif opcao == 2:
            print("\n===== MOVIMENTAÇÕES DO NADADOR =====\n")

            codigo = solicitar_codigo()
            if codigo is None:
                continue

            if consultar_nadador(codigo) is None:
                print("\nNadador não encontrado.\n")
                continue

            lista = movimentacoes_por_nadador(codigo)

            if not lista:
                print("\nNenhuma movimentação encontrada para esse código.\n")
                continue

            imprimir_cabecalho_movimentacoes()
            for movimentacao in lista:
                imprimir_movimentacao(movimentacao)
            print("")

        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            break
        else:
            opcao_invalida()


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu_principal():
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
            menu_toalhas()
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

menu_principal()