# ============================================================
# ESTUDO DE CASO: Nado Livre — Sistema de Controle de Toalhas
#
# Integrantes:
# 202610411100xx - Andrew
# 202610411100xx - Arthur
# 202610411100xx - Marcus
# ============================================================

# Nós escolhemos que, ao escolher uma das opções do menu, o submenu seja repetido até o usuário escolher uma opção válida do submenu e concluir a ação corretamente, pois, caso ele queira voltar para o menu principal, basta escolher a opção 0 - Voltar


codigos = []
nomes = []
quantidades = []
historico_movimentacoes = [] # opção 3
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

    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opção inválida. Por favor, digite um número.\n")
        continue

    if opcao < 0 or opcao > 3:
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
                print("Opção inválida. Por favor, digite um número.\n")
                continue

            if opcao < 0 or opcao > 4:
                print("Opção inválida. Por favor, selecione um número do submenu.\n")
                continue

            elif opcao == 1:
                print("\n===== CADASTRO DE NADADOR =====\n")
                try:
                    cod_input = int(input("Digite o código do nadador: "))
                except ValueError:
                    print("Código inválido! Digite um número válido.\n")
                    continue

                if cod_input not in codigos:
                    nome_input = input("Registre seu nome: ").strip().title()
                else:
                    print("Nadador já cadastrado! Tente outro nome.\n")
                    continue

                if nome_input:
                    codigos.append(cod_input)
                    quantidades.append(0)
                    nomes.append(nome_input)
                    print(f"Nadador {nome_input} cadastrado com sucesso!\n")
                else:
                    print("Nome inválido! Não é possível cadastrar um nadador sem nome.\n")


            elif opcao == 2:
                print("\n" + " NADADORES ".center(55, '=') + "\n")
                
                if len(codigos) > 0:
                    print(f"{'Código':<10}{'Nome':<35}{'Toalhas':>10}")
                    print("-" * 55)
                    for i in range(len(codigos)):
                        print(f"{codigos[i]:<10}{nomes[i]:<35}{quantidades[i]:>10}")
                    print("")
                else:
                    print("Nenhum nadador cadastrado no sistema.\n")


            elif opcao == 3:
                print("\n===== CONSULTAR NADADOR =====\n")
                try:
                    consultar_codigo = int(input("Digite o código do nadador: "))
                except ValueError:
                    print("Código inválido! Digite um número.\n")
                    continue

                if consultar_codigo in codigos:
                    print("\nNadador encontrado:\n")
                    index = codigos.index(consultar_codigo)
                    print(f"{'Código':<10}{'Nome':<35}{'Toalhas':>10}")
                    print("-" * 55)
                    print(f"{codigos[index]:<10}{nomes[index]:<35}{quantidades[index]:>10}\n")
                else:
                    print(f"\nNadador com código {consultar_codigo} não encontrado.\n")


            elif opcao == 4:
                print("\n===== PESQUISAR NADADOR =====\n")
                consultar_nome = input("Digite o nome ou parte do nome: ").strip()

                # Evita nomes idênticos (adiciona duas verificações: um para o nome completo e outro para parte do nome)
                lista_buscar_nome = []
                for i in range(len(nomes)):
                        if consultar_nome.lower() in nomes[i].lower():
                            lista_buscar_nome.append(i)

                if len(lista_buscar_nome) > 0:
                    if len(lista_buscar_nome) == 1:
                        print("\nNadador encontrado:\n")
                    else:
                        print("\nNadadores encontrados:\n")
                    
                    print(f"{'Código':<10}{'Nome':<35}{'Toalhas':>10}")
                    print("-" * 55)
                    for i in lista_buscar_nome:
                        print(f"{codigos[i]:<10}{nomes[i]:<35}{quantidades[i]:>10}")
                    print("")
                else:
                    print(f"\nNenhum nadador encontrado com o nome '{consultar_nome}'.\n")


            elif opcao == 0:
                print("Voltando ao menu principal...\n")
                break 


    elif opcao == 2:
        while True:
            print("\n========== TOALHAS ==========\n")
            print("1 - Retirar toalhas")
            print("2 - Devolver toalhas")
            print("3 - Consulta toalhas em uso")
            print("4 - Consultar toalhas disponíveis")
            print("0 - Voltar")

            try:
                opcao = int(input("\nEscolha uma opção: "))
            except ValueError:
                print("Opção inválida. Digite um número.\n")
                continue

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

                if cod_input in codigos:
                    if quantidade <= 0:
                        print("Quantidade inválida. Digite um número maior que zero.\n")
                    elif quantidade > toalhas_disponiveis:
                        print(f"\nEstoque insuficiente para {quantidade} toalha(s).")
                        print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
                    else:
                        indice = codigos.index(cod_input)
                        quantidades[indice] += quantidade
                        toalhas_disponiveis -= quantidade
                        print("\nRetirada registrada com sucesso!")
                        print(f"Toalhas disponíveis no estoque: {toalhas_disponiveis}\n")
                        print(f"Retirada de {quantidade} toalha(s) pelo nadador {nomes[indice]} (Código: {cod_input})\n")
                        
                        # Salva no histórico
                        historico_movimentacoes.append(f"RETIRADA : {quantidade} toalha(s) - Nadador: {nomes[indice]} (Cód: {cod_input})")
                else:
                    print(f"Código '{cod_input}' não encontrado!\n")


            elif opcao == 2:
                print("\n===== DEVOLUÇÃO DE TOALHAS =====\n")
                try:
                    cod_input = int(input("Digite o código do nadador: "))
                except ValueError:
                    print("Código inválido! Digite um número.\n")
                    continue

                if cod_input in codigos:
                    indice = codigos.index(cod_input)
                    if quantidades[indice] == 0:
                        print(f"O nadador {nomes[indice]} (Código: {cod_input}) não possui toalhas para devolver.\n")
                    else:
                        try:
                            quantidade = int(input(f"Nadador possui {quantidades[indice]} toalhas. Quantas deseja devolver? "))
                        except ValueError:
                            print("Valor inválido! Digite um número.\n")
                            continue

                        if quantidade <= 0:
                            print("Quantidade inválida. Digite um número maior que zero.\n")
                        elif quantidade > quantidades[indice]:
                            print(f"Erro: O nadador {nomes[indice]} possui apenas {quantidades[indice]} toalhas.\n")
                        else:
                            quantidades[indice] -= quantidade
                            toalhas_disponiveis += quantidade
                            print(f"\nDevolução de {quantidade} toalha(s) pelo nadador {nomes[indice]} (Código: {cod_input})")
                            print("Devolução registrada com sucesso! Movimentação concluída.\n")
                            
                            # Salva no histórico
                            historico_movimentacoes.append(f"DEVOLUÇÃO: {quantidade} toalha(s) - Nadador: {nomes[indice]} (Cód: {cod_input})")
                else:
                    print(f"Código '{cod_input}' não encontrado!\n")


            elif opcao == 3:
                print("\n" + " TOALHAS EM USO ".center(55, '=') + "\n")
                if toalhas_disponiveis < TOTAL_TOALHAS:
                    print(f"{'Código':<10}{'Nome':<35}{'Toalhas':>10}")
                    print("-" * 55)
                    for i in range(len(nomes)):
                        if quantidades[i] > 0:
                            print(f"{codigos[i]:<10}{nomes[i]:<35}{quantidades[i]:>10}")
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
       pass


    elif opcao == 0:
        print("Saindo do sistema...")
        break