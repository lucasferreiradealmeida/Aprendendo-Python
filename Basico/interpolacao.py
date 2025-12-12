# Interpolação básica de strings 
# s - string
# d e i - int
# f - float
# x e X -Hexadecimal(ABCDEF123456789)

nome = 'Lucas'
preco = 1000.4387421
variavel = '%s o preço é R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500,1500))