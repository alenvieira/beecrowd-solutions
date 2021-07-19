value = float(input())
msg = 'Fora de intervalo'
if (value >= 0 and value <= 25):
    msg = 'Intervalo [0,25]'
else:
    for i1, i2 in [[25,50], [50,75], [75,100]]:
        if value > i1 and value <= i2:
            msg = 'Intervalo ({},{}]'.format(i1,i2)
print(msg)
