n = int(input())
values = [int(input()) for _ in range(n)]
values_10_20 = [value for value in values if value >= 10 and value <= 20]
print('{} in'.format(len(values_10_20)))
print('{} out'.format(len(values) - len(values_10_20)))
