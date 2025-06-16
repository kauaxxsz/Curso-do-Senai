# Escreva um programa que pede ao usuário dois números e exiba no final a soma deles:
# OUTPUT ESPERADO:

# Digite um número: 10
# Digite outro número: 30
# A soma entre 10 e 30 é: 40


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',40*'-','|')
print('|',15*'-','CALCULAR', 15*'-','|')
print('|',40*'-','|')
numero1=float(input('| Digite um número: '))
numero2=float(input('| Digite outro número: '))
soma=numero1+numero2
resultado=round(soma,2)
print()
print('|',40*'-','|')
print(f'| A soma entre {numero1} e {numero2} é: {resultado}')
print('|',40*'-','|')