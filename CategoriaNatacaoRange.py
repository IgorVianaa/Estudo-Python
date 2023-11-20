from datetime import date

nome = str(input('Qual o seu nome? '))
nasc = int(input('Em que ano você nasceu? '))
ano = date.today().year

idade = ano - nasc

mirim = range(1,10)
infantil = range(10,15)
junior = range(15,20)
senior = range(20,26)

if idade in mirim:
    print(f'Sua idade é {idade} e sua categoria é MIRIM')

elif idade in infantil:
    print(f'Sua idade é {idade} e sua categoria é INFANTIL!')

elif idade in junior:
    print(f'Sua idade é {idade} e sua categoria é JUNIOR!')

elif idade in senior:
    print(f'Sua idade é {idade} e sua categoria é SÊNIOR!')

else:
    print(f'Sua idade é {idade} e sua categoria é MASTER!')