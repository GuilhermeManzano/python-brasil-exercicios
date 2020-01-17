s = float(input('Qual o salário do colaborador? R$ '))
if s <= 280:
    print(f'O valor do salário do colaborador irá passar de R$ {s} para R$ {s*1.20:.2f}, com o reajuste de 20%')
elif s <= 700:
    print(f'O valor do salário do colaborador irá passar de R$ {s} para R$ {s*1.15:.2f}, com o reajuste de 15%')
elif s <= 1500:
    print(f'O valor do salário do colaborador irá passar de R$ {s} para R$ {s*1.10:.2f}, com o reajuste de 10%')
else:
    print(f'O valor do salário do colaborador irá passar de R$ {s} para R$ {s*1.05:.2f}, com o reajuste de 5%')
