# Escreva um programa que pede que o usuário informe uma senha.
# O código deve comparar a senha informada pelo usuário com uma senha pré-definida no código armazenada em uma variável 
# Depois o código deve informar se a senha é correta ou incorreta.

# OUTPUT ESPERADO
# Exemplo 1:

# Digite a senha: 123123
# Senha incorreta

# Exemplo 2:

# Digite a senha: AC12
# Senha correta

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print('|',60*'-','|')
print('|',21*'-','SISTEMA DE SENHAS',20*'-','|')
print('|',60*'-','|')
senha_2=input('| Informe a senha: ')
senha=('123123')
print('|')
if senha_2==senha:
    print('| Senha correta :)')
else:
    print('| Senha incorreta :(')
print('|',60*'-','|')