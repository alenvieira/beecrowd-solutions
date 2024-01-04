while True:
    l, r = list(map(int, input().split()))
    if l == 0 or r == 0:
        break
    elif l > 0 and r > 0:
        print('primeiro')
    elif l < 0 < r:
        print('segundo')
    elif l < 0 and r < 0:
        print('terceiro')
    elif l > 0 > r:
        print('quarto')
