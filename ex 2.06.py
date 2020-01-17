maior = 0
for c in range(1, 4):
    n = int(input(f'Digite o {c}° número: '))
    if c == 1:
        maior = n
    else:
        if n > maior:
            maior = n
print(f'O maior número digitado foi {maior}')
