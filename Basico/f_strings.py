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