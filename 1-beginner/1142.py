n = int(input())
n1 = 1
for _ in range(n):
    n2, n3 = n1 + 1, n1 + 2
    print('{} {} {} PUM'.format(n1, n2, n3))
    n1 = n3 + 2
