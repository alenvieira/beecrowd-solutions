# 1.Álcool 2.Gasolina 3.Diesel 4.Fim)
n1 = 0
n2 = 0
n3 = 0
while True:
    n = input()
    if n == '4':
        break
    elif n == '1':
        n1 += 1
    elif n == '2':
        n2 += 1
    elif n == '3':
        n3 += 1
print('MUITO OBRIGADO')
print('Alcool: {}'.format(n1))
print('Gasolina: {}'.format(n2))
print('Diesel: {}'.format(n3))
