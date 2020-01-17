menor = nome = 0
for c in range(1, 4):
    n = int(input(f'Digite o preço do {c}° produto: R$ '))
    if c == 1:
        menor = n
        nome = c
    else:
        if n < menor:
            menor = n
            nome = c
print(f'O melhor produto a se comprar é o {nome}° produto.')
