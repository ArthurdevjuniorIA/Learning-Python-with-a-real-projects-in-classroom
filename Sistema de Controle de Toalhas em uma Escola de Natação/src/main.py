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
    print("="*33)
    print(f"{'NADO LIVRE':^33}")
    print("="*33+"\n")
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

            opcao = int(input("\nEscolha uma opção: "))

            if not (0 <= opcao <= 4):
                    print("Opção inválida. Por favor, selecione um número do submenu.\n")
                    continue


            if opcao == 1:
                print("\n===== CADASTRO DE NADADOR =====\n")
                cod_input = int(input("Código: "))
                

                if cod_input not in codigos:
                    nome_input = input("Nome: ").strip().title()

                        # Validação: verifica se o nome não está vazio
                    if nome_input.strip():

                        # Deixa as primeiras letras do nome em maiúsculo e as registra na lista logo após

                        codigos.append(cod_input)
                        quantidades.append(0)
                        nomes.append(nome_input)
                        print("Nadador cadastrado com sucesso!\n")
                        break

                    else:
                        print("Dados inválidos! Tente novamente.\n")


                else:
                    print("Código já cadastrado! Tente novamente.\n")


            elif opcao == 2:
                print(f"\n{" NADADORES ".center(63, "=")}\n")
                
                if len(codigos) > 0:
                    print(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
                    print("-" * 63)

                    for i in range(len(codigos)):
                        print(f"{codigos[i]:<8}{nomes[i]:<35}{quantidades[i]:>8}")
                    print("")
                    break
                else:
                    print("Nenhum nadador cadastrado.\n")


            elif opcao == 3:
                print("\n===== CONSULTAR NADADOR =====\n")

                consultar_codigo = int(input("Digite o código do nadador: "))

                if consultar_codigo in codigos:
                    print("\nNadador encontrado:\n")

                    index = codigos.index(consultar_codigo)

                    print(f"{'Código':<7} {'Nome':<33} {'Toalhas':>7}")
                    print("-" * 63)
                    print(f"{codigos[index]:<7} {nomes[index]:<33} {quantidades[index]:>7}\n")
                    break

                else:
                    print("\nNadador não encontrado.\n")


            elif opcao == 4:
                print("\n===== PESQUISAR NADADOR =====\n")

                consultar_nome = input("Digite o nome ou parte do nome: ")

                lista_buscar_nome = [nomes.index(nome) for nome in nomes if consultar_nome.lower() in nome.lower()]

                if len(lista_buscar_nome) > 0:
                    if len(lista_buscar_nome) == 1:
                        print("\nNadador encontrado:\n")

                    else:
                        print("\nNadadores encontrados:\n")
                    print(f"{'Código':<7} {'Nome':<33} {'Toalhas':>7}")
                    print("-" * 63)

                    for i in lista_buscar_nome:
                        print(f"{codigos[i]:<8}{nomes[i]:<35}{quantidades[i]:>8}")
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
                                    nome = nadador["nome"]
                                    break
                            nadador["toalhas"] += quantidade
                            toalhas_disponiveis -= quantidade
                            print("\nRetirada registrada com sucesso!")
                            print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
                            print(f"Retirada de {quantidade} toalha(s) pelo nadador {nome} (Código: {cod_input})\n")
                            
                            # Salva no histórico
                            historico_de_cada = {"codigo": cod_input, "nome": nome, "toalhas": nadador["toalhas"], "acao": "Retirada"}
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
                                toalhas = nadador["toalhas"]
                                break
    
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
                                nadador["toalhas"] -= quantidade
                                toalhas_disponiveis += quantidade
                                print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nome} (Código: {cod_input})")
                                print("Devolução registrada com sucesso! Movimentação concluída.\n")
                                
                                # Salva no histórico
                                historico_de_cada = {"codigo": cod_input, "nome": nome, "toalhas": nadador["toalhas"], "acao": "Devolução"}
                                historico_movimentacoes.append(historico_de_cada)
                    else:
                        print(f"Código '{cod_input}' não encontrado!\n")
    
    
                elif opcao == 3:
                    print("\n" + " TOALHAS EM USO ".center(55, '=') + "\n")
    
                    if toalhas_disponiveis < TOTAL_TOALHAS:
                        print(f"{'Código':<10}{'Nome':<35}{'Toalhas':>8}")
                        print("-" * 55)
                        for nadador in nadadores:
                            if nadador["toalhas"] > 0:
                                print(f"{nadador["codigo"]:<10}{nadador["nome"]:<35}{nadador["toalhas"]:>8}")
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
        sub_opcao = int(input("Escolha uma opção: "))
        if not (0 <= sub_opcao <= 2):
            print("Essa opção é inválida")
            continue
        
        
        if sub_opcao == 0:
            break


        elif sub_opcao == 1:
            print(f"\n{'Ordem':<6}{'Código':>8}  {'Nadador':<15}{'Operação':>12}{'Quantidade':>12}")
            print("-" * 57)
            
            for idx, item in enumerate(historico_movimentacoes, start=1):
                # Garante leitura correta mesmo se houver lista aninhada antiga
                reg = item[0] if isinstance(item[0], list) else item
                print(f"{idx:<6}{reg["codigo"]:>8}  {reg["nome"]:<15}{reg["acao"]:>12}{reg["quantidade"]:>12}")
            print("")


        elif sub_opcao == 2:
            # Na opção 2 - Consultar movimentações do nadador do submenu Movimentações, nós preferimos que fosse solicitado o código do nadador, pois é único para cada nadador
            
            consultar_codigo = int(input("Digite o código que você deseja consultar: "))
            print(f"\n{'Ordem':<6}{'Código':>8}  {'Nadador':<15}{'Operação':>12}{'Quantidade':>12}")
            print("-" * 57)

            for index, item in enumerate(historico_movimentacoes, start=1):
                reg = item[0] if isinstance(item[0], list) else item

                if consultar_codigo == reg[1]:
                    print(f"{idx:<6}{reg["codigo"]:>8}  {reg["nome"]:<15}{reg["acao"]:>12}{reg["quantidade"]:>12}")
            print("")
    elif opcao == 0:
        print("Saindo do sistema...")
        break
