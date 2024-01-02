n = int(input())
for _ in range(n):
    l, r = sorted(list(map(int, input().split())))
    if l % 2 == 0:
        odds = list(range(l + 1, r, 2))
    else:
        odds = list(range(l + 2, r, 2))
    print(sum(odds))
