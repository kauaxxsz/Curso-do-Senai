# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print('|',60*'-','|')
print('|',21*'-','SISTEMA DE PROVAS',20*'-','|')
print('|',60*'-','|')
nome=input('| Nome do aluno: ')
prova1=float(input('| Nota da primeira prova: '))
prova2=float(input('| Nota da segunda prova: '))
prova3=float(input('| Nota da terceira prova: '))
media=(prova1+prova2+prova3)/3
resultado=round(media,2)
print('|',60*'-','|')
print(f'| Aluno: {nome}')
print(f'| Média: {resultado}')
if resultado>=5:
    print('| Aluno aprovado :)')
else:
    print('| Aluno reprovado')
print('|',60*'-','|')