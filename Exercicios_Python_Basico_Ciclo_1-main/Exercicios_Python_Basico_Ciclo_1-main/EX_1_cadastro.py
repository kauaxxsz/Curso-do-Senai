# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|', 50*'-','|')
print('|',20*"-","CADASTRO",20*"-","|")
print('|', 50*'-','|')
nome=input('| Informe seu Nome: ')
idade=int(input('| Informe sua Idade: '))
email=input('| Informe o seu Email: ')
senha=input('| Informe a sua Senha: ')
print('|', 50*'-','|')
print()
print('|',15*"-","USUÁRIO CADASTRADO",15*"-","|")
print(f'| Seja bem vindo(a) {nome}!')
print(f'| Email: {email}')
print('|', 50*'-','|')