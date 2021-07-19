values = input()
a, b, c , d = [int(value) for value in values.split(' ')]
if (b > c and d > a and c+d > a+b and c+d > 0 and a+b > 0 and a % 2 == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
    
