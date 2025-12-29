"""
1️⃣ Pirâmide numérica avançada

Peça um número n ao usuário e imprima uma pirâmide assim (exemplo n = 5):

1
22
333
4444
55555


Depois, imprima a pirâmide invertida:

55555
4444
333
22
1


📌 Restrição:

Use apenas for

Não use multiplicação de strings ('a' * n)
"""

numero = int(input("Digite um numero: "))
lista = []
print_numero = 0
for i in range(0,numero,1):
    lista = [i]
    for j in len(lista):
        lista.append(i)
        print(f'{lista}')
    
