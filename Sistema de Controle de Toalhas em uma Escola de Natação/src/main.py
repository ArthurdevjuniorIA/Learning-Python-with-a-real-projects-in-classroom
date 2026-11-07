nadadores = []
historico_movimentacoes = []
TOTAL_TOALHAS = 30
toalhas_disponiveis = TOTAL_TOALHAS
contador_id = 1


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


# ALTERADO: a docstring dizia que retornava None, mas a função retorna uma lista
# (que pode ser vazia).
def buscar_nadador_por_nome(consultar_nome, nadadores):
    """Retorna a lista de nadadores cujo nome contém o texto buscado (lista vazia se nenhum)."""
    resultados = [n for n in nadadores if consultar_nome in n['nome'].lower()]
    return resultados


def registrar_movimentacao(nadador, quantidade, acao):
    """Adiciona uma retirada ou devolução ao histórico."""
    historico_movimentacoes.append({
        'codigo': nadador['codigo'],
        'nome': nadador['nome'],
        'toalha': quantidade,
        'acao': acao,
    })


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


def imprimir_movimentacao(ordem, item):
    print(f"{ordem:<7}{item['codigo']:<8}{item['nome']:<21}{item['acao']:<15}{item['toalha']:>10}")


# ------------------------------------------------------------
# NADADORES
# ------------------------------------------------------------

def cadastro_nadador(nome, nadadores):
    global contador_id

    if not nome:
        return None

    codigo = contador_id
    contador_id += 1  # Incrementa o contador de ID para o próximo nadador
    nadadores.append({'codigo': codigo, 'nome': nome, 'toalha': 0})
    return codigo


def listar_nadadores(nadadores):
    print(f"\n{' NADADORES '.center(51, '=')}\n")

    if nadadores:
        imprimir_tabela_nadadores(nadadores)
    else:
        print("Nenhum nadador cadastrado.\n")


def consultar_nadadores(codigo, nadadores):
    encontrado = buscar_nadador_por_codigo(codigo, nadadores)
    return encontrado


def pesquisar_nadadores(consultar_nome, nadadores):
    resultados = buscar_nadador_por_nome(consultar_nome, nadadores)
    return resultados


def exibir_menu_nadadores():
    print("\n========== NADADORES ==========\n")
    print("1 - Cadastrar nadador")
    print("2 - Consultar nadadores")
    print("3 - Consultar nadador por código")
    print("4 - Pesquisar nadador por nome")
    print("0 - Voltar")


# ALTERADO: só a indentação (alinhada de 4 em 4 espaços) e as linhas em branco
# soltas. A lógica é a mesma.
def menu_nadadores(nadadores):
    while True:
        exibir_menu_nadadores()

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            cabecalho("\n===== CADASTRO DE NADADOR =====\n")
            nome = input("Nome: ").strip().title()
            codigo = cadastro_nadador(nome, nadadores)

            if codigo is None:
                print("Dados inválidos! O nome não pode ser vazio.\n")
            else:
                print(f"\nNadador cadastrado com sucesso! Código: {codigo}\n")

        elif opcao == 2:
            listar_nadadores(nadadores)

        elif opcao == 3:
            cabecalho("\n===== CONSULTAR NADADOR =====\n")
            codigo = solicitar_codigo()
            if codigo is None:
                continue

            encontrado = consultar_nadadores(codigo, nadadores)
            if encontrado:
                print("\nNadador encontrado:\n")
                imprimir_tabela_nadadores([encontrado])
            else:
                print("\nNadador não encontrado.\n")

        elif opcao == 4:
            cabecalho("\n===== PESQUISAR NADADOR =====\n")
            consultar_nome = input("Digite o nome ou parte do nome: ").strip().lower()
            resultados = pesquisar_nadadores(consultar_nome, nadadores)
            if resultados:
                imprimir_tabela_nadadores(resultados)
            else:
                print("\nNenhum nadador encontrado.\n")

        elif opcao == 0:
            break
        else:
            opcao_invalida()


# ------------------------------------------------------------
# TOALHAS
# ------------------------------------------------------------

def retirar_toalhas(nadador, quantidade, toalhas_disponiveis):
    """Tenta retirar toalhas para o nadador.
    Retorna (sucesso, toalhas_disponiveis_atualizado)."""
    if quantidade > toalhas_disponiveis:
        return False, toalhas_disponiveis

    nadador['toalha'] += quantidade
    registrar_movimentacao(nadador, quantidade, "Retirada")
    return True, toalhas_disponiveis - quantidade


def submenu_retirada_toalhas(toalhas_disponiveis, nadadores):
    cabecalho("\n===== RETIRADA DE TOALHAS =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return toalhas_disponiveis

    nadador = buscar_nadador_por_codigo(codigo, nadadores)
    if nadador is None:
        print(f"Código '{codigo}' não encontrado!\n")
        return toalhas_disponiveis

    quantidade = solicitar_quantidade("Quantidade de toalhas a retirar: ")
    if quantidade is None:
        return toalhas_disponiveis

    sucesso, toalhas_disponiveis = retirar_toalhas(nadador, quantidade, toalhas_disponiveis)

    if sucesso:
        print("\nRetirada registrada com sucesso!")
        print(f"Retirada de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
    else:
        print(f"\nEstoque insuficiente para {quantidade} toalha(s).")

    print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
    return toalhas_disponiveis


def devolver_toalhas(nadador, quantidade, toalhas_disponiveis):
    """Tenta devolver toalhas do nadador ao estoque.
    Retorna (sucesso, toalhas_disponiveis_atualizado)."""
    if quantidade > nadador['toalha']:
        return False, toalhas_disponiveis

    nadador['toalha'] -= quantidade
    registrar_movimentacao(nadador, quantidade, "Devolução")
    return True, toalhas_disponiveis + quantidade


def submenu_devolucao_toalhas(toalhas_disponiveis, nadadores):
    cabecalho("\n===== DEVOLUÇÃO DE TOALHAS =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return toalhas_disponiveis

    nadador = buscar_nadador_por_codigo(codigo, nadadores)
    if nadador is None:
        print(f"Código '{codigo}' não encontrado!\n")
        return toalhas_disponiveis

    if nadador['toalha'] == 0:
        print(f"O nadador {nadador['nome']} (Código: {codigo}) não possui toalhas para devolver.\n")
        return toalhas_disponiveis

    quantidade = solicitar_quantidade(
        f"Nadador possui {nadador['toalha']} toalha(s). Quantas deseja devolver? "
    )
    if quantidade is None:
        return toalhas_disponiveis

    sucesso, toalhas_disponiveis = devolver_toalhas(nadador, quantidade, toalhas_disponiveis)

    if sucesso:
        print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nadador['nome']} (Código: {codigo})")
        print("Devolução registrada com sucesso! Movimentação concluída.\n")
    else:
        print(f"Erro: O nadador {nadador['nome']} possui apenas {nadador['toalha']} toalha(s).\n")

    return toalhas_disponiveis


# ALTERADO: função NOVA. Só faz o filtro (sem print e sem input) e devolve a lista
# de nadadores que estão com toalha. Recebe 'nadadores' por parâmetro.
def filtrar_nadadores_com_toalhas(nadadores):
    """Retorna a lista de nadadores que estão com toalhas."""
    return [n for n in nadadores if n['toalha'] > 0]


# ALTERADO: agora usa a função de filtro acima, a docstring diz o que a função
# realmente faz (imprime), o parâmetro foi renomeado para 'toalhas_disponiveis'
# e removi o 'return toalhas_em_uso' do final, que ninguém usava.
def listar_toalhas_em_uso(toalhas_disponiveis, nadadores):
    """Imprime os nadadores que estão com toalhas e o estoque disponível."""
    print("\n" + " TOALHAS EM USO ".center(51, '=') + "\n")

    com_toalhas = filtrar_nadadores_com_toalhas(nadadores)

    if com_toalhas:
        imprimir_tabela_nadadores(com_toalhas)
        print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
    else:
        print("Nenhum nadador está com toalhas no momento.\n")


def exibir_menu_toalhas():
    print("\n=========== TOALHAS ===========\n")
    print("1 - Retirar toalhas")
    print("2 - Devolver toalhas")
    print("3 - Consultar toalhas em uso")
    print("4 - Consultar toalhas disponíveis")
    print("0 - Voltar")


# ALTERADO: agora recebe 'nadadores' por parâmetro (antes usava a global sem avisar),
# o parâmetro 'toalhas_em_uso' virou 'toalhas_disponiveis' (é isso que ele guarda)
# e os comentários foram corrigidos.
def menu_toalhas(toalhas_disponiveis, nadadores):
    while True:
        exibir_menu_toalhas()

        opcao = solicitar_opcao_menu()

        if opcao == 1:
            # Guarda em toalhas_disponiveis o que sobrou no estoque depois da retirada
            toalhas_disponiveis = submenu_retirada_toalhas(toalhas_disponiveis, nadadores)

        elif opcao == 2:
            # Guarda em toalhas_disponiveis o estoque atualizado depois da devolução
            toalhas_disponiveis = submenu_devolucao_toalhas(toalhas_disponiveis, nadadores)

        elif opcao == 3:
            # Lista os nadadores que estão com toalha
            listar_toalhas_em_uso(toalhas_disponiveis, nadadores)

        elif opcao == 4:
            # Mostra o estoque na tela
            print("\n" + " ESTOQUE DE TOALHAS ".center(51, '=') + "\n")
            print(f"Toalhas disponíveis: {toalhas_disponiveis} de {TOTAL_TOALHAS}\n")

        elif opcao == 0:
            # Devolve o valor final atualizado para quem chamou o menu_toalhas
            return toalhas_disponiveis

        else:
            opcao_invalida()


# ------------------------------------------------------------
# MOVIMENTAÇÕES
# ------------------------------------------------------------

def consultar_movimentacoes(historico_movimentacoes):
    cabecalho("\n===== MOVIMENTAÇÕES =====")

    if not historico_movimentacoes:
        print("\nNenhuma movimentação registrada.\n")
        return

    imprimir_cabecalho_movimentacoes()
    for ordem, item in enumerate(historico_movimentacoes, start=1):
        imprimir_movimentacao(ordem, item)
    print("")


# ALTERADO: função NOVA. Só faz o filtro (sem print e sem input). Mantém a ordem
# original de cada movimentação no histórico geral.
def filtrar_movimentacoes_por_codigo(historico_movimentacoes, codigo):
    """Retorna uma lista de (ordem, item) com as movimentações do nadador."""
    return [
        (ordem, item)
        for ordem, item in enumerate(historico_movimentacoes, start=1)
        if item['codigo'] == codigo
    ]


# ALTERADO: o filtro saiu daqui e foi para a função acima.
# Esta função ficou só com a parte da tela (pedir o código e imprimir).
def consultar_movimentacoes_nadadores(historico_movimentacoes):
    cabecalho("\n===== MOVIMENTAÇÕES DO NADADOR =====\n")

    codigo = solicitar_codigo()
    if codigo is None:
        return

    movimentacoes = filtrar_movimentacoes_por_codigo(historico_movimentacoes, codigo)

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
            opcao_invalida()


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
        # ALTERADO: agora passa 'nadadores' para o menu_toalhas
        toalhas_disponiveis = menu_toalhas(toalhas_disponiveis, nadadores)
    elif opcao == 3:
        menu_movimentacoes(historico_movimentacoes)
    elif opcao == 0:
        print("Saindo do sistema... Até logo!")
        break
    else:
        opcao_invalida()
