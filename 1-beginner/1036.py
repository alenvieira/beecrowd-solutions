values = input()
a, b, c = [float(value) for value in values.split(' ')]
delta = (b ** 2) - (4 * a * c)
if delta < 0 or a != 0:
    print('Impossivel calcular')
else:
    x1 = (-b + (delta**0.5)) / (2 * a)
    x2 = (-b - (delta**0.5)) / (2 * a)
    print('R1 = {:.5f}'.format(x1))
    print('R2 = {:.5f}'.format(x2))
