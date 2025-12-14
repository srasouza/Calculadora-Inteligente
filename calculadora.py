# Insira o número a ser calculado
num1 = input('Digite o primeiro número: ')
operacao = input('Digite o operador (* / - +): ')
num2 = input('Digite o segundo número: ')

# Conversão para número float
num1_convert = float(num1)
num2_convert = float(num2)

# Critérios para os operadores
if operacao == "*":
    resultado = num1_convert * num2_convert
    print('Resultado:', resultado)

elif operacao == "+":
    resultado = num1_convert + num2_convert
    print('Resultado:', resultado)

elif operacao == "-":
    resultado = num1_convert - num2_convert
    print('Resultado:', resultado)

elif operacao == "/":
    resultado = num1_convert / num2_convert
    print('Resultado:', resultado)

else:
    print('Operação Inválida!')

