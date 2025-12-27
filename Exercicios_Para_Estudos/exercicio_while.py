"""
🟦 Questão 1 – Contagem controlada

Faça um programa que peça um número inteiro positivo ao usuário e imprima todos os números de 1 até esse número, usando while.

👉 Exemplo:
Entrada: 5
Saída:
"""

# numero = input("digite um inteiro positivo: ")
# if numero.isdigit():
#     numero = int(numero)
#     indice = 1
#     while indice <= numero:
#         print(indice)
#         indice += 1
# else:
#     print("Você não digitou um número inteiro positivo.")


"""
🟦 Questão 2 – Soma até zero

Faça um programa que:

Leia números inteiros do usuário

Some todos os números digitados

O programa deve parar quando o usuário digitar 0

Ao final, mostre a soma total
"""


# numero_total = 0
# while True:
#     numero = int(input("digite um inteiro positivo (Digite 0 para sair): "))
#     if numero == 0:
#         break
#     numero_total += numero
#     print("Numero total: ", numero_total)


"""
🟦 Questão 3 – Validação de senha

Crie um programa que:

Peça uma senha ao usuário

Enquanto a senha digitada for diferente de "1234", continue pedindo

Quando a senha correta for digitada, exiba:

Acesso permitido
"""

# senha = None
# while senha != '1234':
#     senha = input("digite uma senha: ")
# print("Acesso permitido")


"""
🟦 Questão 4 – Contar pares e ímpares

Faça um programa que:

Leia números inteiros até o usuário digitar 0

Conte quantos números pares e quantos ímpares foram digitados

Mostre o resultado no final
"""


# par = 0
# impar = 0
# while True:
#     numero = int(input("digite um inteiro positivo (Digite 0 para sair): "))
#     if numero == 0:
#         break
#     elif numero % 2 == 0:
#         par += 1
#     elif numero % 2 != 0:
#         impar += 1
# print(f'Impares: {impar}')
# print(f'Pares: {par}')


"""
🟦 Questão 5 – Média de notas

Faça um programa que:

Leia notas (valores inteiros)

O usuário digita -1 para encerrar

Calcule e mostre a média das notas digitadas

⚠️ Considere que pelo menos uma nota válida será digitada.
"""

# contador = 0
# soma = 0
# while True:
#     numero = int(input("digite um inteiro positivo (Digite -1 para sair): "))
#     if numero == -1:
#         break
#     soma += numero
#     contador += 1
#     media = soma / contador
#     print("Média:", media)

"""
🔴 Questão 1 – Média com validação

Faça um programa que:

Leia números inteiros positivos

Ignore números negativos (não entram na média)

O programa termina quando o usuário digitar 0

No final, mostre a média apenas dos números válidos
"""
soma = 0
contador = 0
while True:
    numero = int(input("digite um inteiro positivo (Digite 0 para sair): "))
    if numero < 0:
        continue
    elif numero == 0:
        break
    soma += numero
    contador += 1
media = soma/contador
print("Média:", media)