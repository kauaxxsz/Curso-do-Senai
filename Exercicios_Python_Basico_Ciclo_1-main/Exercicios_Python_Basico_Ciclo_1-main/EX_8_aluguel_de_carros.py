# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',65*'-','|')
print('|',23*'-','ALUGUEL DE CARROS',23*'-','|')
print('|',65*'-','|')
dias=int(input('| Por quantos dias o carros foi alugado? '))
km_rodado=float(input('| Quantos km o carro rodou? '))
calculo=60*dias+0.15*km_rodado
resultado=round(calculo,2)
print('|')
print(f'| Você andou {km_rodado}km por {dias} dias, então o preço a pagar é R${resultado}.')
print('|',65*'-','|')