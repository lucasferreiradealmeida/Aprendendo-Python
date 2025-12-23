"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de 
inserir,apagar e listar valores da sua lista
Não permita que o programe quebre com 
erros de indices inexistentes na lista
"""

lista = []
while True:
    try:
        print('-------------------')
        print("1 - Voce deseja inserir? ")
        print("2 - Voce deseja apagar? ")
        print("3 - Voce deseja listar valores? ")
        opcao = int(input("Você escolhe qual opção? "))
        print('-------------------')

        if opcao == 1:
            numero_inserir = input("Qual numero voce deseja inserir? ")
            lista.append(numero_inserir)

        elif opcao == 2:
                try:
                    if lista == []:
                        print("Lista vazia")
                        continue
                    numero_apagar = int(input("Qual indice voce deseja apagar? "))
                    del lista[numero_apagar]
                    print("Apagou!")
                except:
                    print("Não foi possivel apagar este indice")
                    continue
        
        elif opcao == 3:
            if lista == []:
                print("Lista vazia")
            else:
                for indice, nome in enumerate(lista):
                    print(f'{indice} {nome}')
        else:
            print("Digite numeros validos")
    except :
        print("Digite apenas números")
        continue
    

    