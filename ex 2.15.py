l1 = float(input('Digite o 1° lado do triângulo: '))
l2 = float(input('Digite o 2° lado do triângulo: '))
l3 = float(input('Digite o 3° lado do triângulo: '))
if l1 + l2 > l3 or l2 + l3 > l1 or l1 + l3 > l2:
    print('Os três lados formam um triângulo do tipo: ', end='')
    if l1 == l2 == l3:
        print('Equilátero')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os três lados \033[35mnão\033[m formam um triânuglo!')
