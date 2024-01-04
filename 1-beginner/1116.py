n = int(input())
for _ in range(n):
    l, r = list(map(int, input().split()))
    if r == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(l/r))
