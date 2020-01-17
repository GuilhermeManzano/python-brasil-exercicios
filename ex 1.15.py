s = float(input('Quanto você ganha por hora? R$ '))
h = int(input('Número de horas trabalhadas no mês? '))
salariobru = s * h
ir = salariobru * 0.11
inss = salariobru * 0.08
sindicato = salariobru * 0.05
salario = salariobru - ir - inss - sindicato
print(f'Você ganha R$ {s} por hora e trabalhou {h} horas este mês, seu salário bruto foi de R$ {salariobru} e seu salário líquido será de R$ {salario:.2f}')
