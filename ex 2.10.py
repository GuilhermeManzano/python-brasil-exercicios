t = str(input('Qual turno você estuda (M-matutino ou V-Vespertino ou N- Noturno)? ')).upper().strip()
while t != 'M' or t != 'V' or t != 'N':
    t = str(input('Valor inválido! \nQual turno você estuda (M-matutino ou V-Vespertino ou N- Noturno)? ')).upper().strip()
    else:
        if t == 'M':
            print('Bom Dia!')
        if t == 'V':
            print('Boa Tarde!')
        if t == 'N':
            print('Boa Noite!')
        break
print('Boas aulas!')
