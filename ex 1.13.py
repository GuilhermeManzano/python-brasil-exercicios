s = True
h = float(input('Digite a sua altura (em metros): '))
while s != 'MF':
    s = str(input('É homem ou mulher? [M/F] ')).upper().strip()
    if s == 'F':
        peso = (62.1*h) - 44.7
        print(f'O seu peso ideal é {peso:.2f} kg')
        break
    if s == 'M':
        peso = (72.7*h) - 58
        print(f'O seu peso ideal é {peso:.2f} kg')
        break
