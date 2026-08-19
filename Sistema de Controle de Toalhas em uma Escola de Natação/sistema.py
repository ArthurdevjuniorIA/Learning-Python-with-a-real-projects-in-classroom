import time
codigos = []
nomes = []
quantidades = [ ]
codigo_quem_que_retirou_toalhas = [ ]
quantas_toalhas_retiradas = {retirada for retirada in codigo_quem_que_retirou_toalhas : quantidade }
nova_quantida = [ ]
toalhas_disponiveis = 30
def exibir_menu():
    print("=================================")
    print("""
███╗░░██╗░█████╗░██████╗░░█████╗░  ██╗░░░░░██╗██╗░░░██╗██████╗░███████╗
████╗░██║██╔══██╗██╔══██╗██╔══██╗  ██║░░░░░██║██║░░░██║██╔══██╗██╔════╝
██╔██╗██║███████║██║░░██║██║░░██║  ██║░░░░░██║╚██╗░██╔╝██████╔╝█████╗░░
██║╚████║██╔══██║██║░░██║██║░░██║  ██║░░░░░██║░╚████╔╝░██╔══██╗██╔══╝░░
██║░╚███║██║░░██║██████╔╝╚█████╔╝  ███████╗██║░░╚██╔╝░░██║░░██║███████╗
╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░  ╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝
    """)
    time.sleep(
        2
    )
while True:
    print("=================================")
    print("NADO LIVRE")
    print("=================================\n")
    print("1 - Cadastrar nadador")
    print("2 - Consultar nadadores")
    print("3 - Registrar retirada de toalhas")
    print("4 - Consultar toalhas em uso")
    print("5- Devolução de toalhas")
    print("0 - Sair")
while True:
    exibir_menu()

    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número.")
        time.sleep(
            1.5
        )
        continue

    if opcao == 1:
        print("\n===== CADASTRO DE NADADOR =====\n")

        try:
            cod_input = int(input("Código: "))
        except ValueError:
            print("Código inválido. Digite um número.")
            continue


        nome_input = input("Nome: ")


        # Validação: verifica se o código é número e se o nome não está vazio
        if nome_input.strip() != "":
            codigos.append(cod_input)
            nomes.append(nome_input)
            quantidades.append(0)
            print("\nNadador cadastrado com sucesso!\n")
            time.sleep(
                1.5
            )
        else:
            print("\nDados inválidos! Tente novamente.\n")




    elif opcao == 2:
        print("\n========= NADADORES =========\n")
        if len(codigos) > 0:
            for i in range(len(codigos)):
                print(f"{codigos[i]} - {nomes[i]}")
            print("")
            time.sleep(
                2
            )
        else:
            print("Nenhum nadador cadastrado.\n")




    elif opcao == 3:
        try:
            cod_input = int(input("\nCódigo: "))
            quantidade = int(input("Quantidade: "))
        
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue


        if cod_input in codigos:
            if quantidade <=0:
                print("Quantidade inválida. Digite um número maior que zero.")
                time.sleep( 
                    1.5
                )
            elif quantidade > toalhas_disponiveis:
                print("\nEstoque insuficiente.")
                print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
                time.sleep(
                    1.5
                )
            else:
                indice = codigos.index(cod_input)
                quantidades[indice] += quantidade
                toalhas_disponiveis -= quantidade
                print("\nRetirada registrada com sucesso!")
                print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
                time.sleep(
                    1.5
                )
                codigo_quem_que_retirou_toalhas.append(cod_input)     
        else:
            print("Código não encontrado!")
            time.sleep(
                1.5
            )


    elif opcao == 4:
        print("\n======= TOALHAS EM USO ========\n")

        if len(nomes) > 0:

            for i in range(len(nomes)):
                if quantidades[i] > 0:
                    print(f"{nomes[i]} - {quantidades[i]} toalha(s)")
            print(f"\nToalhas disponíveis: {toalhas_disponiveis}\n")
            time.sleep(
                2
            )

        else:
            print("Nenhum nadador cadastrado.")
            time.sleep(
                1.5
            )
    elif opcao == 5:
        cod_input = int(input("Digite o código: "))
        for i in range(len(codigo_quem_que_retirou_toalhas)):
            if cod_input in codigo_quem_que_retirou_toalhas:
                print(f"Você já retirou {codigo_quem_que_retirou_toalhas[i]}")
                quantas_devolver = int(input("Digite quantas toalhas você deseja devolver: "))
                if quantas_devolver>quantidades[i]:
                    print("Você não pode devolver mais toalhas do que tem emprestado")
                else:
                    quantidade_nova = quantidades[i]- quantas_devolver
                    nova_quantida.append(quantidade_nova)

   
    elif opcao == 0:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, selecione um número do menu.")