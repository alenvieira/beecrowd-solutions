while True:
    l, r = sorted(list(map(int, input().split())))
    if l <= 0 or r <= 0:
        break
    numbers = list(range(l, r + 1))
    print('{} Sum={}'.format(' '.join(map(str, numbers)), sum(numbers)))
