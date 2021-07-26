values = [input() for _ in range(6)]
number_values = [int(value) if value.isnumeric() else 0 for value in values]
count_positive = len([value for value in number_values if value > 0])
print('{} valores positivos'.format(count_positive))
