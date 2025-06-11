# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',60*'-','|')
print('|',25*'-','DESCONTO', 25*'-','|')
print('|',60*'-','|')
print()
print('|',60*'-','|')
produto=float(input('| Qual o preço do produto? '))
porcentagem=float(input('| Qual a porcentagem de desconto? '))
desconto=produto*(porcentagem/100)
print('|')
print(f'| O poduto que custa R${produto} terá R${desconto} de desconto.')
print('|',60*'-','|')