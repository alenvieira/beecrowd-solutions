x, y = [float(value) for value in input().split(' ')]
msg = 'Origem'
if x < 0 and y < 0:
    msg = 'Q3'
elif x < 0 and y > 0:
    msg = 'Q2'
elif x > 0 and y < 0:
    msg = 'Q4'
elif x > 0 and y > 0:
    msg = 'Q1'
elif x == 0 and y != 0:
    msg = 'Eixo Y'
elif x != 0 and y == 0:
    msg = 'Eixo X'
print('{}'.format(msg))
