# AND

entrada = input('[E]ntrar  [S]air:')
senha_digitada = input('Senha:')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    
#Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)


# OR

entrada = input('[E]ntrar  [S]air:')
senha_digitada = input('Senha:')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else: 
    print('Sair')
    
senha = input('Senha: ') or 'Sem senha'
print(senha)
    

# NOT

senha= input('Senha: ')

if not senha:
    print('Você não digitou nada')
    
print(not True)
print(not False)


# IN E NOT IN

#  1  2  3  4  5
#  L  U  C  A  S
# -5 -4 -3 -2 -1
 
nome = 'Lucas'
print(nome[2])
print(nome[-3])
print('c' in nome)
print('z' in nome)
print(10 * '-')
print('c' not in nome)
print('z' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
    