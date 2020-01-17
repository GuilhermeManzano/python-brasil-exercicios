p = float(input('Digite o peso do peixe (kg): '))
if p > 50:
    limite = p - 50
    multa = limite * 4
    print(f'O peso do peixe é de {p} e está ACIMA DO LIMITE PERMITIDO EM LEI!')
    print(f'O valor da multa a pagar é de R$ {multa} e o peso foi excedido em {limite} kg.')
else:
    print(f'O peso do peixe é de {p} e está dentro dos limites estabelecidos em lei.')
