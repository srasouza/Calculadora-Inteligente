# Insira o número a ser calculado
try:
  num1 = input ('Digite o número ')
  operacao = input ('Digite o operador(* / - +): ')
  num2 = input ('Digite o número ')

  #Conversão pra número inteiro
  num1_convert = float (num1)
  num2_convert = float (num2)

  #Critérios para os operadores
  if operacao == "*":
    resultado = num1_convert * num2_convert
    print('Resultado:', resultado)
  if operacao == "+":
    resultado = num1_convert + num2_convert
    print('Resultado:', resultado)
  elif operacao == "-":
    resultado = num1_convert - num2_convert
    print('Resultado:', resultado)
  elif operacao == "/":
    if num2_convert != 0:
      resultado = num1_convert / num2_convert 
    else:
      print('Erro divisão por zero')
      exit ()
  else:
    print ('Resultado: ', resultado)

#Caso o usuário digite um caractere inválido
except: ValueError
print('Digite apenas números válidos(use ponto para decimais).')
