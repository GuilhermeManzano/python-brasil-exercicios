maior = menor = meio = c = 0
while c != 3:
    n = int(input(f'Digite o {c+1}° número: '))
    if c == 0:
        maior = menor = meio = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        else:
            meio = n
    c += 1
print(maior, meio, menor)
