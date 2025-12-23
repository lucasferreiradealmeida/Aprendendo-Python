lista = ['maria','lucas','luiz']
lista.append("João")

lista_enumerada = list(enumerate(lista))

print(lista_enumerada )
for indice, nome in enumerate(lista):
    print(indice, nome)