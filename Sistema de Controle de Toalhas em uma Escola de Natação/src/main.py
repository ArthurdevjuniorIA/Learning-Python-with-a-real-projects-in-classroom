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

# FUNÇÃO PARA SOLICITAR A OPÇÃO DO MENU

def solicitar_opcao_menu():
    try: 
        opcao = int(input("\nEscolha uma opção: "))
        return opcao
    except ValueError:
        return -1

# FUNÇÃO PARA BUSCAR NADADOR PELO CÓDIGO

def buscar_nadador_por_codigo(cod_input):
    for nadador in nadadores:
        if nadador['codigo'] == cod_input:
            return nadador
    return None

# FUNÇÕES DOS SUBMENUS


def printar_menu_nadadores():
    print("\n========== NADADORES ==========\n")
    print("1 - Cadastrar nadador")
    print("2 - Consultar nadadores")
    print("3 - Consultar nadador por código")
    print("4 - Pesquisar nadador por nome")
    print("0 - Voltar")
    while True:
        printar_menu_nadadores()

        opcao = solicitar_opcao_menu()

        if not (0 <= opcao <= 4):
            print("Opção inválida. Por favor, selecione um número do submenu.\n")
            continue
        def opcao_1_Menu_nadadores():
            print("\n===== CADASTRO DE NADADOR =====\n")
            try:
                cod_input = int(input("Código: "))
            except ValueError:
                print("Código não válido. Tente novamente.")
                return
            if cod_input<=0:
                print("O código não pode ser menor que 0\n")
                return


            if not any(nadador['codigo'] == cod_input for nadador in nadadores):
                nome_input = input("Nome: ").strip().title()

                if nome_input:
                    nadador = {
                    'codigo': cod_input,
                    'nome': nome_input,
                    'toalha': 0,
                    }
                    nadadores.append(nadador)
                    print("Nadador cadastrado com sucesso!\n")
                else:
                    print("Dados inválidos! Tente novamente.\n")
            else:
                print("Código já cadastrado! Tente novamente.\n")
        def opcao_2_Menu_nadadores():
            print(f"\n{' NADADORES '.center(63, '=')}\n")
            
            if len(nadadores) > 0:
                print(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
                print('-' * 63)
                for nadador in nadadores:
                    print(f"{nadador['codigo']:<8}{nadador['nome']:<35}{nadador['toalha']:>8}")
                print("")
            else:
                print("Nenhum nadador cadastrado.\n")
        def opcao_3_menu_nadadores():

            print("\n===== CONSULTAR NADADOR =====\n")
            try:
                cod_input = int(input("Digite o código do nadador: "))
            except ValueError:
                print("Código não válido.")
                continue

            encontrado = buscar_nadador_por_codigo(cod_input)
            
            if encontrado:
                print("\nNadador encontrado:\n")
                print(f"{'Código':<7} {'Nome':<33} {'Toalhas':>7}")
                print("-" * 63)
                print(f"{encontrado['codigo']:<7} {encontrado['nome']:<33} {encontrado['toalha']:>7}\n")
            else:
                print("\nNadador não encontrado.\n")

        def opcao_4_menu_nadadores():
            print("\n===== PESQUISAR NADADOR =====\n")
            consultar_nome = input("Digite o nome ou parte do nome: ").strip()

            resultados = [nadador for nadador in nadadores if consultar_nome.lower() in nadador['nome'].lower()]
            if resultados:
                if len(resultados) == 1:
                    print("\nNadador encontrado:\n")
                else:
                    print("\nNadadores encontrados:\n")
                
                print(f"{'Código':<7} {'Nome':<33} {'Toalhas':>7}")
                print("-" * 63)
                for nadador in resultados:
                    print(f"{nadador['codigo']:<8}{nadador['nome']:<35}{nadador['toalha']:>8}")
                print("")
            else:
                print("\nNenhum nadador encontrado.\n")
        if opcao == 1:
            opcao_1_Menu_nadadores()
        elif opcao == 2:
            opcao_2_Menu_nadadores()
        elif opcao == 3:
            opcao_3_menu_nadadores()
        elif opcao == 4:
            opcao_4_menu_nadadores()
        elif opcao == 0:
            break 


def menu_toalhas():
    # Modificar a variável global de toalhas
    global toalhas_disponiveis 
    
    while True:
        print("\n========== TOALHAS ==========\n")
        print("1 - Retirar toalhas")
        print("2 - Devolver toalhas")
        print("3 - Consulta toalhas em uso")
        print("4 - Consultar toalhas disponíveis")
        print("0 - Voltar")

        opcao = solicitar_opcao_menu()

        if opcao < 0 or opcao > 4:
            print("Opção inválida. Por favor, selecione um número do submenu.\n")
            continue

        if opcao == 1:
            print("\n===== RETIRADA DE TOALHAS =====\n")
            try:
                cod_input = int(input("Código do nadador: "))
                quantidade = int(input("Quantidade de toalhas a retirar: "))
            except ValueError:
                print("Valor inválido. Digite um número.\n")
                continue
            
            if cod_input in [nadador['codigo'] for nadador in nadadores]:
                if quantidade <= 0:
                    print("Quantidade inválida. Digite um número maior que zero.\n")
                elif quantidade > toalhas_disponiveis:
                    print(f"\nEstoque insuficiente para {quantidade} toalha(s).")
                    print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
                else:
                    nadador = buscar_nadador_por_codigo(cod_input)
                    nadador['toalha'] += quantidade
                    toalhas_disponiveis -= quantidade
                    nome = nadador['nome']

                    print("\nRetirada registrada com sucesso!")
                    print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
                    print(f"Retirada de {quantidade} toalha(s) pelo nadador {nome} (Código: {cod_input})\n")
                    
                    historico_de_cada = {"codigo": cod_input, "nome": nome, "toalha": quantidade, "acao": "Retirada"}
                    historico_movimentacoes.append(historico_de_cada)
            else:
                print(f"Código '{cod_input}' não encontrado!\n")

        elif opcao == 2:
            print("\n===== DEVOLUÇÃO DE TOALHAS =====\n")
            try:
                cod_input = int(input("Digite o código do nadador: "))
            except ValueError:
                print("Código inválido! Digite um número.\n")
                continue
            
            if cod_input in [nadador['codigo'] for nadador in nadadores]:
                nadador = buscar_nadador_por_codigo(cod_input)
                nome = nadador['nome']
                toalhas = nadador['toalha']
                nadador_ref = nadador
                        
                if toalhas == 0:
                    print(f"O nadador {nome} (Código: {cod_input}) não possui toalhas para devolver.\n")
                else:
                    try:
                        quantidade = int(input(f"Nadador possui {toalhas} toalhas. Quantas deseja devolver? "))
                    except ValueError:
                        print("Valor inválido! Digite um número.\n")
                        continue
                    
                    if quantidade <= 0:
                        print("Quantidade inválida. Digite um número maior que zero.\n")
                    elif quantidade > toalhas:
                        print(f"Erro: O nadador {nome} possui apenas {toalhas} toalhas.\n")
                    else:
                        nadador_ref["toalha"] -= quantidade
                        toalhas_disponiveis += quantidade
                        print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nome} (Código: {cod_input})")
                        print("Devolução registrada com sucesso! Movimentação concluída.\n")
                        
                        historico_de_cada = {"codigo": cod_input, "nome": nome, "toalha": quantidade, "acao": "Devolução"}
                        historico_movimentacoes.append(historico_de_cada)
            else:
                print(f"Código '{cod_input}' não encontrado!\n")

        elif opcao == 3:
            print("\n" + " TOALHAS EM USO ".center(55, '=') + "\n")
            if toalhas_disponiveis < TOTAL_TOALHAS:
                print(f"{'Código':<10}{'Nome':<35}{'Toalhas':>8}")
                print("-" * 55)
                for nadador in nadadores:
                    if nadador['toalha'] > 0:
                        print(f"{nadador['codigo']:<10}{nadador['nome']:<35}{nadador['toalha']:>8}")
                print(f"\nToalhas disponíveis no estoque: {toalhas_disponiveis}\n")
            else:
                print("Nenhum nadador está com toalhas no momento.\n")

        elif opcao == 4:
            print("\n" + " ESTOQUE DE TOALHAS ".center(55, '=') + "\n")
            print(f"Toalhas disponíveis: {toalhas_disponiveis} de {TOTAL_TOALHAS}\n")

        elif opcao == 0:
            print("Voltando ao menu principal...\n")
            break


def menu_movimentacoes():
    while True:
        print("\n======== MOVIMENTAÇÕES ========\n")
        print("1 - Consultar movimentações")
        print("2 - Consultar movimentações do nadador")
        print("0 - Voltar\n")

        opcao = solicitar_opcao_menu()
        
        if not (0 <= opcao <= 2):
            print("Opção inválida. Por favor, selecione um número do submenu.\n")
            continue
        
        if opcao == 0:
            break

        elif opcao == 1:
            print(f"\n{'Ordem':<6}{'Código':>8}  {'Nadador':<15}{'Operação':>12}{'Quantidade':>12}")
            print('-' * 57)
        
            for idx, item in enumerate(historico_movimentacoes, start=1):
                print(f"{idx:<6}{item['codigo']:>8}  {item['nome']:<15}{item['acao']:>12}{item['toalha']:>12}")
            print("")

        elif opcao == 2:
            try:
                cod_input = int(input("Digite o código que você deseja consultar: "))
            except ValueError:
                print("Opção inválida. Tente um número do menu.")
                continue

            print(f"\n{'Ordem':<6}{'Código':>8}  {'Nadador':<15}{'Operação':>12}{'Quantidade':>12}")
            print('-' * 57)

            for idx, item in enumerate(historico_movimentacoes, start=1):
                if cod_input == item['codigo']:
                    print(f"{idx:<6}{item['codigo']:>8}  {item['nome']:<15}{item['acao']:>12}{item['toalha']:>12}")
            print("")

# MENU PRINCIPAL

def menu_principal():
        print('=' * 33)
        print(f"{'NADO LIVRE':^33}")
        print('=' * 33 +"\n")
        print("1 - Nadadores")
        print("2 - Toalhas")
        print("3 - Movimentações")
        print("0 - Sair") 

# PROGRAMA PRINCIPAL

while True:
    menu_principal()

        # CHAMADA
        if opcao == 1:
            printar_menu_nadadores()
        elif opcao == 2:
            menu_toalhas()
        elif opcao == 3:
            menu_movimentacoes()
        elif opcao == 0:
            print("Saindo do sistema... Até logo!")
            break 

    opcao = solicitar_opcao_menu()

    if not (0 <= opcao <= 3):
        print("Opção inválida. Por favor, selecione um número do menu.\n")
        continue


    # CHAMADA
    if opcao == 1:
        menu_nadadores()
    elif opcao == 2:
        menu_toalhas()
    elif opcao == 3:
        menu_movimentacoes()
    elif opcao == 0:
        print("Saindo do sistema... Até logo!")
        break