n = int(input())
values = [int(input()) for _ in range(n)]
for value in values:
    msg = 'ODD '
    if value % 2 == 0:
        msg = 'EVEN '
    if value < 0:
        msg = msg + 'NEGATIVE'
    elif value > 0:
        msg = msg + 'POSITIVE'
    else:
        msg = 'NULL'
    print(msg)
