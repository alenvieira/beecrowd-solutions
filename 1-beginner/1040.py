n1, n2, n3, n4 = [float(value) for value in input().split(' ')]
avg = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)
msg = 'Aluno reprovado.'
if avg >= 7.0:
    msg = 'Aluno aprovado.'
elif avg >= 5.0 and avg <= 6.9:
    msg = 'Aluno em exame.'
print('Media: {:.1f}'.format(avg))
print('{}'.format(msg))
if avg >= 5.0 and avg < 6.9:
    new_n = float(input())
    print('Nota do exame: {:.1f}'.format(new_n))
    avg = (avg + new_n) / 2    
    if avg >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(avg))
