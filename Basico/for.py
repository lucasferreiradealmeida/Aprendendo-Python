# Primeiro video (Introdução ao for / in)

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')


# Segundo video (range + for)

'''
for + range
range -> range(start,stop,step)
'''


numeros = range(0,10,2)

for numero in numeros:
    print(numero)


# Terceiro video (next, iter, iterável e iterador)


"""
Iteravel -> str,range, etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""
# o que isso é por baixo dos panos
for letra in texto 
texto = 'Luiz' # iteravel
iterador = iter(texto) #iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break

# é a mesma coisa de cima 
for letra in texto
    print(letra)
    

# Quarto video (continue, break, else, etc)

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print("i é 8, seu else não executará")
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso')