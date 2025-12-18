"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Primeira Questão

numero = input('Digite um numero inteiro: ')
try:
    numero = int(numero)

    if numero % 2 == 0:
        print('Numero par')
    elif numero % 2 != 0:
        print('Numero impar')
    
except:
    print('isso não é numero inteiro')

# Segunda Questão

hora = input('Me fale a hora: ')
try:
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print(f"Bom dia são: {hora} horas")
    elif hora >= 12 and hora <= 17:
        print(f"Bom tarde são: {hora} horas")
    elif hora >= 18 and hora <= 23:
        print(f"Bom noite são: {hora} horas")
    else:
            print("Hora inválida")
except:
    print("Isso não é uma hora válida")

# Terceira Questão

nome = input("Fale o seu primeiro nome: ")
if len(nome) <= 4:
    print("Seu nome é curto")
elif len(nome) == 5 or len(nome) == 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")


