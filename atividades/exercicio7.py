""" Calculadora com while """
while True:
    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o segundo numero: ')
    operador = input("qual operador voce escolhe (+-/*): ")
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos == None:
        print("Um ou ambos os numeros digitados são invalidos")
        continue

    if operador == '+':
        resultado = numero_1_float + numero_2_float
        print("Resultado:", resultado)

    elif operador == '-':
        resultado = numero_1_float - numero_2_float
        print("Resultado:", resultado)

    elif operador == '/':
        resultado = numero_1_float / numero_2_float
        print("Resultado:", resultado)

    elif operador == '*':
        resultado = numero_1_float * numero_2_float
        print("Resultado:", resultado)

    else:
        print('Operador invalido')

    sair = input("Quer sair? [S] [N] ")
    sair = sair.lower()
    if sair == 's':
        break
    elif sair == 'n':
        continue
    else:
        print("voce digitou uma opção inexistente")
        