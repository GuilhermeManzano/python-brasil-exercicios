
t = float(input('Qual é o tamanho do arquivo? (em MB) '))
v = float(input('Qual a velocidade de um link de internet? (em Mpbs) '))
d = t / v
print(f'O download levará {d/60:.2f} minutos para ser concluído')
