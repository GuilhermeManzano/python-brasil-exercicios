n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media < 4:
    print(f'A média do aluno foi {media} e ele tirou o conceito E')
elif media >= 4:
    print(f'A média do aluno foi {media} e ele tirou o conceito D')
elif media >= 6:
    print(f'A média do aluno foi {media} e ele tirou o conceito C')
elif media >= 7.5:
    print(f'A média do aluno foi {media} e ele tirou o conceito B')
elif media >= 9 and media <= 10:
    print(f'A média do aluno foi {media} e ele tirou o conceito A')
else:
    print('Valores inválidos!')
