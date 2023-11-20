#Calcule o IMC
#imc = peso / (altura*altura)

print('\33[1:33mVamos ver como está sua medida corporal?\33[m')



peso = float(input('Qual o seu peso hoje?: '))
altura = float(input('Qual a sua altura?: '))

imc = round(peso / (altura*altura))

print(f'\33[1;34;107mSeu índice de massa corporal do momento é:\33[m {imc}')

if imc < 18.5:
    print(f'Seu imc é {imc}, está ABAIXO do peso')
elif imc < 25:
    print(f'Seu imc é {imc}, seu peso está IDEAL')
elif imc < 30:
    print(f'Seu imc é {imc}, está SOBREPESO')
elif imc < 40:
    print(f'Seu imc é {imc}, está com OBESIDADE')
else:
    print(f'Seu imc é {imc}, está com OBESIDADE MÓRBIDA')


