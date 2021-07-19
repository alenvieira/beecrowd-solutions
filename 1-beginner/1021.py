value = float(input())
print('NOTAS:')
for cell in [100, 50, 20, 10, 5, 2]:
    print('{} nota(s) de R$ {},00'.format(int(value/cell), cell))
    value = value % cell
print('MOEDAS:')
for coin in [1, 0.5, 0.25, 0.10, 0.05, 0.01]:
    print('{} moeda(s) de R$ {:.2f}'.format(int(value/coin), coin).replace('.',','))
    value = round(value % coin, 2)
