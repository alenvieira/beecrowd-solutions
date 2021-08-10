for x in range(0, 15):
    i = 1 + (x // 3 * 2)
    j = (3 * ((i//2) + 2)) + i - x 
    print('I={} J={}'.format(i, j))
