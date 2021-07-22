hour_start, hour_end = [int(value) for value in input().split(' ')]
hours = ((24 - hour_start) + hour_end) % 24
if hours == 0:
    hours = 24
print('O JOGO DUROU {} HORA(S)'.format(hours))
