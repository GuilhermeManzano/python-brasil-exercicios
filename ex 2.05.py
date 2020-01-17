#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med >= 7 and med != 10:
    print(f'A média do aluno foi {med} e ele está \033[1;32;41mAPROVADO!!\033[m')
if med < 7:
    print(f'A média do aluno foi {med} e ele está \033[1;35;42mREPROVADO!!\033[m')
if med == 10:
    print(f'A média do aluno foi {med} e ele está \033[1;32;41mAPROVADO COM DISTIÇÃO!!\033[m')
