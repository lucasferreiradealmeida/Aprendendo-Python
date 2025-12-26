"""
Listas em Python
Tipo List - Mutavél
Suporta vários valores de qualquer tipo
Conhecimento reutilizaveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
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

# Aula 3 (Tipo list)

lista = [10,20,30,40]
lista.append("Luiz")
nome = lista.pop
lista.append(1233)
del lista[-1]
# lista.clear
lista.insert(100,5)
print(lista[4])

# Aula 4 (Concatenando e estendendo)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_a)


# Aula 5 (list e copy)

lista_a = ['Luiz', 'Maria' , 1 , True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = "Qualquer coisa"
print(lista_a)
print(lista_b)

# Aula 6 (for in com tipo list)

lista = ['Maria','Lucas','Juliano']

for name in lista:
    print(name, type(nome))



# Aula 7 (empacotamento e desempacotamento)

_, _, nome, *resto = ['maria','lucas','luiz']
print(nome)

# Aula 8 (Tupla)

"""
Tipo tupla - Uma lista imutavael
"""

nomes = 'maria','lucas','luiz'

print(nomes[-1])
print(nomes)

# Aula 9 (pegar índices)

lista = ['maria','lucas','luiz']
lista.append("João")

lista_enumerada = list(enumerate(lista))

print(lista_enumerada )
for indice, nome in enumerate(lista):
    print(indice, nome)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')


# Aula 10 (split, join e strip)

"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = "Olha só que, coisa interresante"
lista_frases = frase.split(",")
print(lista_frases)

# Aula 11 (Listas dentro de listas)

salas = [
    # 0         1
    ['Maria','Helena',], # 0
    # 0
    ['Elaine'] # 1
    # 0       1      2
    ['Luiz','João','Eduarda',], # 2
]
# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala:
        print(aluno)

# Aula 12 (Desempacotamento)

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

p,b,*_,ap,u = lista
print(p,u,ap)

print('Maria','Helena',1,2,3,'Eduarda')
print(*lista)
print(*string)
print(*tupla)

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

print(*salas, sep='\n')