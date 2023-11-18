print('Vamos calcular a nota Anual de 1 aluno apenas!')

a1 = input('Qual o nome do aluno? ')

b1 = float(input('Nota do primeiro bimestre: '))
b2 = float(input('Nota do segundo bimestre: '))
b3 = float(input('Nota do terceiro bimestre: '))
b4 = float(input('Nota do quarto bimestre: '))

soma = (b1+b2+b3+b4)/4

print(f'A sua média Anual é de {soma}')

if soma >7:
    print(f'Parabéns {a1}, Você está Aprovado')
elif soma >=5 <=6:
    print(f' {a1} Você está de recuperação')
else:
    print(f'Infelizmente {a1}, Está Reprovado')
