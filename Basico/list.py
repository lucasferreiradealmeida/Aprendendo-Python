"""
Listas em Python
Tipo List - Mutavél
Suporta vários valores de qualquer tipo
Conhecimento reutilizaveis - índices e fatiamento
Métodos úteis: append,insert,pop,del,clear,extend +
"""
#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) #falsy
# print(lista,type(lista))

#        0      1     2     3   4
#       -5      4     3     2   1
lista = [123, True,'lucas',1.2,[]]
print(lista[2],type(lista[2]))


# Aula 2 (Tipo list)

#   Create Read Update Delete
#   criar,ler,alterar,apagar = lista[i](CRUD)

lista = [10,20,30,40]
lista[2] = 300
del lista[2] # excluindo o 300
print(lista)
print(lista[2])
lista.append(50) # adiciona no final da lista
lista.pop() # retira o ultimo item da lista
lista.append(60) 
lista.append(70) 
print(lista)