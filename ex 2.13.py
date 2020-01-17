#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

v = int(input('Digite um número de 1 a 7: '))
if v == 1:
    print('Domingo')
elif v == 2:
    print('Segunda')
elif v == 3:
    print('Terça')
elif v == 4:
    print('Quarta')
elif v == 5:
    print('Quinta')
elif v == 6:
    print('Sexta')
elif v == 7:
    print('Sábado')
else:
    print('Inválido!')
