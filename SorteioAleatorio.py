import random

print('Sortear 1 dos 4 alunos para apagar o quadro')

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista = a1, a2, a3 ,a4
sorteado = random.choice(lista)

print(f'O aluno sorteado, foi: {sorteado}')

