values = [int(value) for value in input().split(' ')]
hour_start, minute_start, hour_end, minute_end = values
hours = ((24 - hour_start) + hour_end) % 24
minutes = ((60 - minute_start) + minute_end) % 60
if hour_start == hour_end and minute_start == minute_end:
    hours = 24
if minute_start > minute_end and hours == 0:
    hours = 24
if minute_start > minute_end:
    hours = hours - 1
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hours, minutes))
