n = int(input())
for _ in range(n):
    l, r = list(map(int, input().split()))
    if l % 2 == 0:
        l += 1
    total = 0
    for i in range(l, l+(r * 2), 2):
        total += i
    print(total)
