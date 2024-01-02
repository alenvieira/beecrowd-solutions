while True:
    l, r = list(map(int, input().split()))
    if l == r:
        break
    elif l < r:
        print('Crescente')
    else:
        print('Decrescente')
