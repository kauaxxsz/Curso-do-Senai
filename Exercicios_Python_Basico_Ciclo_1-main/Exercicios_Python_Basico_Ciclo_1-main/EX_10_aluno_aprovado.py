# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',60*'-','|')
print('|',20*'-','SISTEMA DE PROVAS2',20*'-','|')
print('|',60*'-','|')
prova1=float(input('| Informe a nota da primeira prova: '))
prova2=float(input('| Informe a nota da segunda prova: '))
soma=(prova1+prova2)/2
print('|')
print('|  Aluno aprovado? ',soma>=7)
print('|',60*'-','|')