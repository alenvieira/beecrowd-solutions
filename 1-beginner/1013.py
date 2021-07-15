line = input()
(a, b, c) = [int(i) for i in line.split(' ')]
greatest1 = (a + b + abs(a - b)) / 2
greatest2 = int((greatest1 + c + abs(greatest1 - c)) / 2)
print('{} eh o maior'.format(greatest2))
