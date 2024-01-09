x, y = list(map(int, input().split()))
n = y // x
for i in range(n):
    print(*range(i*x+1, 1+(i*x)+x))
