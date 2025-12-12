nome = 'Lucas Ferreira'
altura = 1.73
peso = 70
imc = peso / (altura * altura)

#F-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# SEGUNDA AULA DE F STRINGS


# Formatação básica de strings
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centro
# = - Força o número a aparecer antes dos   zeros
#  Sinal - + ou -
#  Ex.: 0>-100,.1f
#  conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.6371267361821:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print{f'{variavel!r}'}


