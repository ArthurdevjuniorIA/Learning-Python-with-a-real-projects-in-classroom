# ============================================================
# ESTUDO DE CASO: Nado Livre — Sistema de Controle de Toalhas
#
# Integrantes:
# 20261041110027 - Andrew
# 20261041110017 - Arthur
# 20261041110009 - Marcus
# ============================================================

# Nós escolhemos que, ao escolher uma das opções do menu, o submenu seja repetido até o usuário escolher uma opção válida do submenu e concluir a ação corretamente, pois, caso ele queira voltar para o menu principal, basta escolher a opção 0 - Voltar
'''
nadador = {'codigo': codigo, 'nome': nome, 'toalhas': toalhas}

nadador = {
    "codigo": codigo,
    "nome": nome,
    "toalhas": toalhas
}

nadadores.append(nadador)

nadadores = [
    {
        "codigo": codigo,
        "nome": nome,
        "toalhas": toalhas
    }
]
'''

nadadores = []
historico_movimentacoes = []
TOTAL_TOALHAS = 30
toalhas_disponiveis = TOTAL_TOALHAS

while True:
    print('=' * 33)
    print(f"{'NADO LIVRE':^33}")
    print('=' * 33 +"\n")
    print("1 - Nadadores")
    print("2 - Toalhas")
    print("3 - Movimentações")
    print("0 - Sair")


    opcao = int(input("\nEscolha uma opção: "))

    if not (0 <= opcao <= 3):
        print("Opção inválida. Por favor, selecione um número do menu.\n")
        continue

    if opcao == 1:
        while True:
            print("\n========== NADADORES ==========\n")
            print("1 - Cadastrar nadador")
            print("2 - Consultar nadadores")
            print("3 - Consultar nadador por código")
            print("4 - Pesquisar nadador por nome")
            print("0 - Voltar")

            try: 
                opcao = int(input("\nEscolha uma opção: "))

            except ValueError:
                print("Solução inválida. Por favor, escolha um número do menu.")
                continue


            if not (0 <= opcao <= 4):
                print("Opção inválida. Por favor, selecione um número do submenu.\n")
                continue


            if opcao == 1:
                print("\n===== CADASTRO DE NADADOR =====\n")

                try:
                    cod_input = int(input("Código: "))
                except ValueError:
                    print("Código não válido. Tente novamente.")
                    continue

                if not any(nadador['codigo'] == cod_input for nadador in nadadores):
                    # Substitui if "cod_input not in nadadores:"
                    nome_input = input("Nome: ").strip().title()

                    # Validação: verifica se o nome não está vazio
                    if nome_input:

                        # Deixa as primeiras letras do nome em maiúsculo e as registra na lista logo após

                        nadador = {
                        'codigo': cod_input,
                        'nome': nome_input,
                        'toalha': 0,
                        'historico': []
                        }
                        nadadores.append(nadador)
                        print("Nadador cadastrado com sucesso!\n")
                        

                    else:
                        print("Dados inválidos! Tente novamente.\n")


                else:
                    print("Código já cadastrado! Tente novamente.\n")


            elif opcao == 2:
                    print(f"\n{' NADADORES '.center(63, '=')}\n")
                
                    if len(nadadores) > 0:
                        print(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
                        print('-' * 63)

                        for nadador in nadadores:
                            print(f"{nadador['codigo']:<8}{nadador['nome']:<35}{nadador['toalha']:>8}")
                        print("")
                    
                    else:
                        print("Nenhum nadador cadastrado.\n")


            elif opcao == 3:
                    print("\n===== CONSULTAR NADADOR =====\n")

                    consultar_codigo = int(input("Digite o código do nadador: "))


                    encontrado = False 
                    for nadador in nadadores:
                        if nadador['codigo'] == consultar_codigo:
                            encontrado = nadador
                            break
                        

                    if encontrado:
                        print("\nNadador encontrado:\n")
                        print(f"{'Código':<7} {'Nome':<33} {'Toalhas':>7}")
                        print("-" * 63)
                        print(f"{nadador['codigo']:<7} {nadador['nome']:<33} {nadador['toalha']:>7}\n")
                    

                    else:
                        print("\nNadador não encontrado.\n")


            elif opcao == 4:
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


            else:
                    break 


    elif opcao == 2:
            while True:
                print("\n========== TOALHAS ==========\n")
                print("1 - Retirar toalhas")
                print("2 - Devolver toalhas")
                print("3 - Consulta toalhas em uso")
                print("4 - Consultar toalhas disponíveis")
                print("0 - Voltar")
    
                opcao = int(input("\nEscolha uma opção: "))

                
                if opcao < 0 or opcao > 4:
                    print("Opção inválida. Por favor, selecione um número do submenu.\n")
                    continue
    
    
                elif opcao == 1:
                    print("\n===== RETIRADA DE TOALHAS =====\n")
                    try:
                        cod_input = int(input("Código do nadador: "))
                        quantidade = int(input("Quantidade de toalhas a retirar: "))

                    except ValueError:

                        print("Valor inválido. Digite um número.\n")
                        continue
    
                    if cod_input in [nadador["codigo"] for nadador in nadadores]:
                        if quantidade <= 0:
                            print("Quantidade inválida. Digite um número maior que zero.\n")
    
                        elif quantidade > toalhas_disponiveis:
                            print(f"\nEstoque insuficiente para {quantidade} toalha(s).")
                            print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
    
                        else:
                            for nadador in nadadores:
                                if nadador["codigo"] == cod_input:
                                    nadador['toalha'] += quantidade
                                    toalhas_disponiveis -= quantidade
                                    nome = nadador["nome"]
                                    break

                            print("\nRetirada registrada com sucesso!")
                            print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
                            print(f"Retirada de {quantidade} toalha(s) pelo nadador {nome} (Código: {cod_input})\n")
                            
                            # Salva no histórico
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
    
                    if cod_input in [nadador["codigo"] for nadador in nadadores]:
                        for nadador in nadadores:
                            if nadador["codigo"] == cod_input:
                                nome = nadador["nome"]
                                toalhas = nadador["toalha"]
                                
    
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
                                nadador["toalha"] -= quantidade
                                toalhas_disponiveis += quantidade
                                print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nome} (Código: {cod_input})")
                                print("Devolução registrada com sucesso! Movimentação concluída.\n")
                                
                                # Salva no histórico
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
                            if nadador["toalha"] > 0:
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
    
    
    
    elif opcao == 3:
        while True:
            print("\n======== MOVIMENTAÇÕES ========\n")
            print("1 - Consultar movimentações")
            print("2 - Consultar movimentações do nadador")
            print("0 - Voltar\n")

            try:
                sub_opcao = int(input("Escolha uma opção: "))

            except ValueError:
                print("A opção digitada é inválida. Digite um dos números do menu.")
                continue
            if not (0 <= sub_opcao <= 2):
                print("Essa opção é inválida")
                continue
        
        
            if sub_opcao == 0:
                break


            elif sub_opcao == 1:
                print(f"\n{'Ordem':<6}{'Código':>8}  {'Nadador':<15}{'Operação':>12}{'Quantidade':>12}")
                print('-' * 57)
            
                for idx, item in enumerate(historico_movimentacoes, start=1):
                    # Garante leitura correta mesmo se houver lista aninhada antiga
                    reg = item['toalha'] if isinstance(item['toalha'], list) else item
                    print(f"{idx:<6}{reg['codigo']:>8}  {reg['nome']:<15}{reg['acao']:>12}{reg['toalha']:>12}")
                print("")


            elif sub_opcao == 2:
                # Na opção 2 - Consultar movimentações do nadador do submenu Movimentações, nós preferimos que fosse solicitado o código do nadador, pois é único para cada nadador
                try:

                    consultar_codigo = int(input("Digite o código que você deseja consultar: "))

                except ValueError:
                    print("Opção inválida. Tente um número do menu.")
                    continue

                print(f"\n{'Ordem':<6}{'Código':>8}  {'Nadador':<15}{'Operação':>12}{'Quantidade':>12}")
                print('-' * 57)

                for idx, item in enumerate(historico_movimentacoes, start=1):
                    reg = item['toalha'] if isinstance(item['toalha'], list) else item

                    if consultar_codigo == reg['codigo']:
                        print(f"{idx:<6}{reg['codigo']:>8}  {reg['nome']:<15}{reg['acao']:>12}{reg['toalha']:>12}")
                print("")
    elif opcao == 0:
        print("Saindo do sistema...")
        break
        