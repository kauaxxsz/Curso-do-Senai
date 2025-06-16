# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print()
print('Escolha uma opção')
print('1 - Dollar para Real')
print('2 - Real para Dollar')
escolha=int(input('Informe uma das opções: '))
if escolha==1:
    dollar=float(input('Informe a cotação do Dollar: '))
    convercao=float(input('Digite o valor em Dollar a ser convertido em real: '))
    real=dollar*convercao
    resultado=round(real,2)
    print(f'O valor em reais é: {real}')
elif escolha==2:
    real=float(input('Digite o valor em Real a ser convertido em Dollar: '))
    dollar=float(input('Informe a cotação do Dollar: '))
    convercao=real/dollar
    resultado=round(convercao,2)
    print(f' O valor em dólares é $ {convercao}')
else:
    print('ERROOORRRRRR')