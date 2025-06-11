# Escreva um programa que pede ao usuário o valor atual da cotação do dollar e a quantidade de dólares para ser convertido em reais. 
# Depois mostre na tela a conversão.

# OUTPUT ESPERADO:

# Digite a cotação do dollar: 5.60
# Digite o valor em dollar a ser convetido para real: 100
# O valor em reais é:  560.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',60*'-','|')
print('|',20*'-','CONVERÇÃO DOLLAR','|',20*'-')
print('|',60*'-','|')
print()
print('|',60*'-','|')
dollar=float(input('| Informe a cotação do Dollar: '))
convercao=float(input('| Digite o valor em Dollar a ser convertido em real:'))
real=dollar*convercao
print()
print(f'| O valor em reais é: {real}')
print('|',60*'-','|')