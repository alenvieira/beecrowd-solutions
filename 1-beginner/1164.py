n = int(input())
for _ in range(n):
    x = int(input())
    numbers = []
    for i in range(1, x):
        if x % i == 0:
            numbers.append(i)
    if sum(numbers) == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
