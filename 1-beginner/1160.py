n = int(input())
for _ in range(n):
    pa, pb, g1, g2 = input().split()
    pa, pb, g1, g2 , ano = int(pa), int(pb), float(g1), float(g2), 0
    for i in range(1, 102):
        ano = i
        pa += (pa * g1) // 100
        pb += (pb * g2) // 100
        if pa > pb:
            break
    if ano > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(ano))
