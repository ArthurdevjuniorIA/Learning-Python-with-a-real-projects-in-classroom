import time
codigos = []
nomes = []
quantidades = []
toalhas_disponiveis = 30
while True:
    print("=================================")
    print("NADO LIVRE")
    print("=================================\n")
    print("1 - Cadastrar nadador")
    print("2 - Consultar nadadores")
    print("3 - Registrar retirada de toalhas")
    print("4 - Consultar toalhas em uso")
    print("0 - Sair")

# try/except evita que o programa quebre se o usuário digitar algo que não seja número. O Python tenta converter (try) se der erro, executa o "except ValueError" em vez de travar o programa.


    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número.")
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
        if nome_input.strip():
              
            codigos.append(cod_input)
            # Deixa as primeiras letras do nome em maiúsculo e as registra na lista logo após    
            nomes.append(nome_input.title())
            quantidades.append(0)
       
       
            print("Nadador cadastrado com sucesso!\n")
        else:
            print("Dados inválidos! Tente novamente.\n")
       
       
       
       
       
       
       
       
    elif opcao == 2:
        print("\n========================== NADADORES ==========================\n")
        if len(codigos) > 0:
            print(f"{'Código':<8}{'Nome':<35}{'Toalhas'}")
            print("---------------------------------------------------------------")
            for i in range(len(codigos)):
                print(f"{codigos[i]:<7} {nomes[i]:<35} {quantidades[i]}")
            print("")
            time.sleep(2)
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
            print("Código não encontrado!")


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
   
    elif opcao == 0:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, selecione um número do menu.")