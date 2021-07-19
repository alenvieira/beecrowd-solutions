value = int(input())
print(value)
for cell in [100, 50, 20, 10, 5, 2, 1]:
    print('{} nota(s) de R$ {},00'.format(int(value/cell), cell))
    value = value % cell
