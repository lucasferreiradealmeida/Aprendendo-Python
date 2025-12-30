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

# numero = int(input("Digite um numero: "))
# for i in range(1,numero + 1):
#     for j in range(i):
#         print(i, end='') 
#     print()

# print("\nPirâmide invertida:\n")

# for i in range(numero,0,-1):
#     for j in range(i):
#         print(i, end='') 
#     print()
   

"""
2️⃣ Soma ponderada com índices

Dada a lista:

numeros = [10, 20, 30, 40, 50]


Calcule o seguinte somatório:

(10 × 1) + (20 × 2) + (30 × 3) + (40 × 4) + (50 × 5)


📌 Regras:

Não use enumerate

Não use while
"""

# numeros = [10, 20, 30, 40, 50]
# somatorio = 0
# for i in range(0,len(numeros)):
#     somatorio += numeros[i] * (i + 1)
# print(somatorio)


"""
3️⃣ Validação de CPF (parte matemática)

Dado um CPF como string:

cpf = "746824890"


Calcule o primeiro dígito verificador seguindo a regra oficial:

Multiplicadores de 10 até 2

Somatório

Fórmula do dígito

📌 Regras:

Use apenas for

Não use funções prontas

Não use listas auxiliares desnecessárias
"""

# cpf = "746824890"
# multiplicatorio = 0
# multicadores = 10
# somatorio = 0
# for digito in cpf:
#     multiplicatorio = int(digito) * multicadores
#     multicadores -= 1
#     somatorio += multiplicatorio
# somatorio = somatorio * 10
# somatorio = somatorio % 11
# print("0" if somatorio > 9 else somatorio)



"""
4️⃣ Contador de padrões

Dada a string:

texto = "ababcababcab"


Conte quantas vezes o padrão "ab" aparece, inclusive sobreposto.

📌 Exemplo:

"abab" → 2 ocorrências


📌 Regras:

Não use .count()

Use for com controle de índice
"""

# texto = "ababcababcab"
# contador_ab = 0
# for i in range(len(texto) - 1):
#     if texto[i] == 'a':
#             if texto[i+1] == 'b':
#                 contador_ab += 1
# print(contador_ab)


"""
5️⃣ Matriz 3x3 com soma diagonal

Crie uma matriz 3x3 usando for:

1 2 3
4 5 6
7 8 9


Depois:

Some a diagonal principal

Some a diagonal secundária

📌 Regras:

Use for aninhado

Não escreva os valores manualmente
"""
# matriz = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# somatorio = 1


# for i in range(0,3):
#     for j in range(0,3):
#         matriz[i][j] = somatorio
#         somatorio += 1
# soma_principal = matriz[0][0] + matriz[1][1] + matriz[2][2] 
# soma_secundaria = matriz[0][2] + matriz[1][1] + matriz[2][0]
# print(matriz[0])
# print(matriz[1])
# print(matriz[2])
# print(f'Soma diagonal principal:{soma_principal}')
# print(f"Soma diagonal secundária:{soma_secundaria}")


"""
6️⃣ Detecção de números primos em intervalo

Peça dois números inicio e fim ao usuário e imprima todos os números primos nesse intervalo.

📌 Regras:

Use for aninhado

Não use break no primeiro divisor (controle bem a lógica)
"""

numero_1 = int(input("Digite o primeiro numero do intervalo: "))
numero_2 = int(input("Digite o primeiro segundo do intervalo: "))
i = 2

for primo in range(numero_1,numero_2):
    if primo <= 1:
        print(f'o numero {primo} não é primo')
        
    else:
        while True:

            if primo % i == 0:
                print(f'o numero {primo} é primo')

            if primo == i:
                break

            i += 1