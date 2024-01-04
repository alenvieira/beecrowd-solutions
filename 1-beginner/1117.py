n = 0
total = 0
while n < 2:
    user_input = float(input())
    if 0 > user_input or user_input > 10:
        print('nota invalida')
    else:
        total += user_input
        n += 1
print('media = {:g}'.format(total / 2))
