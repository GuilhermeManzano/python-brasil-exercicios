a = int(input('Digite o valor de A: '))
if a == 0:
    print('Como A é igual a 0, a equação não é de segundo grau. \nPrograma encerrado!')
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
delta = (b * b) - (4 * a * c)
if delta < 0:
    print('Como o delta é negativo, a equação não possui raízes reais. \nPrograma encerrado!')
x1 = (-b * delta) / (2 * a)
x2 = (-b * -delta) / (2 * a)
if delta == 0:
    if x1 > 0:
        print(f'Como o delta é igual a 0, a equação possui apenas 1 raíz real, que é {x1} \nPrograma encerrado!')
    if x2 > 0:
        print(f'Como o delta é igual a 0, a equação possui apenas 1 raíz real, que é {x2} \nPrograma encerrado!')
if delta > 0:
    print(f'A equação possuí duas raízes reais, são elas: {x1} e {x2} \nPrograma encerrado!')
