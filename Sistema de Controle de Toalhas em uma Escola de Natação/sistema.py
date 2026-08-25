'''
- Estudo de Caso 2 - Sistema de Controle de Toalhas em uma Escola de Natação
- Componentes do grupo:
    Andrew Rafael 
    Arthur Kauã
    Marcus Paulo 
'''

import time
codigos = []
nomes = []
quantidades = []
TOTAL_TOALHAS = 30
toalhas_disponiveis = TOTAL_TOALHAS
def chamar_tempo():
    time.sleep(
        1.5
    )


while True:
    print("="*33)
    print(f"{"NADO LIVRE":^33}")
    print("="*33+"\n")
    print("1 - Cadastrar nadador")
    print("2 - Toalhas")
    print("3 - Movimentações")
    print("0 - Sair")

# try/except evita que o programa quebre se o usuário digitar algo que não seja número. O Python tenta converter (try) se der erro, executa o "except ValueError" em vez de travar o programa.

    if opcao<3:
        opcao = int(input("\nEscolha uma opção: "))
    else: # Caso o usuário digite uma opção inválida
        print("Opção inválida. Digite um número.\n")
        chamar_tempo()
        continue



    if opcao == 1:
        print("\n===== CADASTRO DE NADADOR =====\n")
        print("1 - Cadastrar nadador")
        print("2 - Consultar nadadores")
        print("3 - Consultar nadador por código")
        print("4 - Pesquisar nadador por nome")
        print("0 - Voltar")
        if cod_input in codigos:
            cod_input = int(input("Código: "))
        else:
            print("Código inválido. Digite um número.\n") # Caso o usuário digite um código inválido
            continue

        if cod_input not in codigos:
            nome_input = input("Nome: ").strip().title()

                # Validação: verifica se o nome não está vazio
            if nome_input.strip():

                # Deixa as primeiras letras do nome em maiúsculo e as registra na lista logo após

                if nome_input not in nomes:
                    codigos.append(cod_input)
                    quantidades.append(0)
                    nomes.append(nome_input)
                    print("Nadador cadastrado com sucesso!\n")
                else:
                    print(f"O nome {nome_input} já está cadastrado no sistema.\n")
            else:
                print("Dados inválidos! Tente novamente.\n")
                chamar_tempo()


        else:
            print("Código já cadastrado! Tente novamente.\n")
            chamar_tempo()
       
       
       
    elif opcao == 2:
        print(f"\n{" NADADORES ".center(63, "=")}\n")

        if len(codigos) > 0:
            print(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
            print("---------------------------------------------------------------")

            for i in range(len(codigos)):
                print(f"{codigos[i]:<8}{nomes[i]:<35}{quantidades[i]:>8}")
            print("")
            time.sleep(2)
        else:
            print("Nenhum nadador cadastrado.\n")
   
  
  
  
    elif opcao == 3:
        try:
            cod_input = int(input("\nCódigo: "))
            quantidade = int(input("Quantidade: "))
        
        except ValueError:
            print("Valor inválido. Digite um número.\n")
            chamar_tempo()
            continue

        if cod_input in codigos:

            if quantidade <=0:
                print("Quantidade inválida. Digite um número maior que zero.\n")
                chamar_tempo()

            elif quantidade > toalhas_disponiveis:
                print("\nEstoque insuficiente.")
                print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
                chamar_tempo()

            else:
                indice = codigos.index(cod_input)
                quantidades[indice] += quantidade
                toalhas_disponiveis -= quantidade
                print("\nRetirada registrada com sucesso!")
                print(f"Toalhas disponíveis: {toalhas_disponiveis}\n")
                chamar_tempo()
        
        else:
            print("Código não encontrado!\n")
            chamar_tempo()




    elif opcao == 4:
        print("\n======================== TOALHAS EM USO ======================\n")
        
        encontrou = False

        print(f"{'Código':<8}{'Nome':<35}{'Toalhas':>8}")
        print("-" * 51)

        for i in range(len(nomes)):
            if quantidades[i] > 0:
                print(f"{codigos[i]:<8}{nomes[i]:<35}{quantidades[i]:>8}")
                time.sleep(
                    2
                )
                encontrou = True
        if not encontrou:
            print("Nenhum nadador cadastrado.\n")
            chamar_tempo()



    elif opcao == 5:
        print("\n===== CONSULTAR NADADOR =====\n")

        consultar_codigo = int(input("Digite o código do nadador: "))

        if consultar_codigo in codigos:
            print("\nNadador encontrado:\n")

            chamar_tempo()
            index = codigos.index(consultar_codigo)

            print(f"{'Código':<7} {'Nome':<33} {'Toalhas':>7}")
            print("---------------------------------------------------------------")
            print(f"{codigos[index]:<7} {nomes[index]:<33} {quantidades[index]:>7}\n")
            time.sleep(2)

        else:
            print("\nNadador não encontrado.\n")
            chamar_tempo()




    elif opcao == 6:
        print("\n===== PESQUISAR NADADOR =====\n")

        consultar_nome = input("Digite o nome ou parte do nome: ")

        lista_buscar_nome = [nomes.index(nome) for nome in nomes if consultar_nome.lower() in nome.lower()]

        if len(lista_buscar_nome) > 0:

            print("\nNadador encontrado:\n")
            print(f"{'Código':<7} {'Nome':<33} {'Toalhas':>7}")
            chamar_tempo()
            print("---------------------------------------------------------------")

            for i in lista_buscar_nome:
                print(f"{codigos[i]:<8}{nomes[i]:<35}{quantidades[i]:>8}")
            print("")
            time.sleep(2)

        else:
            print("\nNenhum nadador encontrado.\n")
            chamar_tempo()

   
    elif opcao == 0:
        print("Saindo do sistema...")
        chamar_tempo()
        break



    else:
        print("Opção inválida. Por favor, selecione um número do menu.\n")
