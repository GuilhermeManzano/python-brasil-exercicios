ir = irsal = inss = fgts = liq = 0
s = float(input('Digite o salário por hora do colaborador: R$ '))
h = float(input('Quantas horas o colaborador trabalhou neste mês? R$ '))
salario = s * h
if salario <= 900:
    irsal = (ir/100) * salario
    inss = salario * 0.1
    fgts = salario * 0.11
    liq = salario - irsal - inss
elif salario <= 1500:
    ir = 5
    irsal = (ir/100) * salario
    inss = salario * 0.1
    fgts = salario * 0.11
    liq = salario - irsal - inss
elif salario <= 2500:
    ir = 10
    irsal = (ir/100) * salario
    inss = salario * 0.1
    fgts = salario * 0.11
    liq = salario - irsal - inss
else:
    ir = 20
    irsal = (ir/100) * salario
    inss = salario * 0.1
    fgts = salario * 0.11
    liq = salario - irsal - inss
print(f'Salário Bruto: ({s} * {h}): R$ {salario}')
print(f'(-) IR {ir}% : R$ {irsal}')
print(f'(-) INSS (10%): R$ {inss}')
print(f'FGTS (11%): R$ {fgts}')
print(f'Total de descontos: R$ {irsal+inss}')
print(f'Salário Líquido: R$ {liq}')
