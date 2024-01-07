n = int(input())
for n1 in range(1, n+1):
    n2, n3 = n1 ** 2, n1 ** 3
    print('{} {} {}'.format(n1, n2, n3))
    print('{} {} {}'.format(n1, n2+1, n3+1))
