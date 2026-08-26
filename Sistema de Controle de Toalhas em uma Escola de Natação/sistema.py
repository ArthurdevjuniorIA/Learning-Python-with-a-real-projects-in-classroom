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
TOTAL_TOALHAS = 30
toalhas_disponiveis = TOTAL_TOALHAS


while True:
    print("="*33)
    print(f"{"NADO LIVRE":^33}")
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

                if cod_input in codigos:
                    cod_input = int(input("Código: "))
                else:
                    print("Código inválido. Digite um número.\n") 
                    continue

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


        if opcao == 1:
            try:
                cod_input = int(input("\nCódigo: "))
                quantidade = int(input("Quantidade: "))
            
            except ValueError:
                print("Valor inválido. Digite um número.\n")
                continue

            if cod_input in codigos:

                if quantidade <=0:
                    print("Quantidade inválida. Digite um número maior que zero.\n")

                elif quantidade > toalhas_disponiveis:
                    print("\nEstoque insuficiente.")
                    print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")

                else:
                    indice = codigos.index(cod_input)
                    quantidades[indice] += quantidade
                    toalhas_disponiveis -= quantidade
                    print("\nRetirada registrada com sucesso!")
                    print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
            
            else:
                print("Código não encontrado!\n")


        elif opcao == 3:
            print(f"\n{" TOALHAS EM USO ".center(60, "=")}\n")

            if toalhas_disponiveis < TOTAL_TOALHAS:
                print(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
                print("-" * 61)

                for i in range(len(nomes)):
                    if quantidades[i] > 0:
                        print(f"{codigos[i]:<8}{nomes[i]:<35}{quantidades[i]:>8}")

                print(f"\nToalhas disponíveis: {toalhas_disponiveis}\n")
            else:
                print("Nenhum nadador retirou toalhas.\n")
            



    elif opcao == 3:




    elif opcao == 0:
        print("Saindo do sistema...")
        break