new_calculate = True
n = 0
total = 0
while True:
    user_input = float(input())
    if new_calculate:
        invalid = 0 > user_input or user_input > 10
        if invalid:
            print('nota invalida')
        else:
            total += user_input
            n += 1
            if n == 2:
                print('media = {:0.2f}'.format(total / 2))
                total, n, new_calculate = 0, 0, False
                print('novo calculo (1-sim 2-nao)')
    else:
        if user_input == 1:
            new_calculate = True
        elif user_input == 2:
            break
        else:
            print('novo calculo (1-sim 2-nao)')

