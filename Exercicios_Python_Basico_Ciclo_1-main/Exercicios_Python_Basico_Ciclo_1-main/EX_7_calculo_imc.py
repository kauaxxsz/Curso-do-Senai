# Escreva um código que pede ao usuário a altura e o peso e faça o cálculo do IMC (Índice de massa corporal) do usuário.
# Dica:
# Para calcular o IMC você deve dividir o peso pela altura ao quadrado
# imc = peso / (altura ** 2)


# OUTPUT ESPERADO:

# Digite sua altura: 1.78
# Digite seu peso: 85
# O seu IMC é: 26.83

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',60*'-','|')
print('|',22*'-','SISTEMA DE IMC',22*'-','|')
print('|',60*'-','|')
altura=float(input('| Digite sua altura: '))
peso=float(input('| Digitr o seu peso: '))
calculo_imc= peso / (altura ** 2)
imc=round (calculo_imc,2)
print('|')
print('| Seu IMC é',imc)
print('|',60*'-','|')