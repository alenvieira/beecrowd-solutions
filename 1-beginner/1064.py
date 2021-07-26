values = [input() for _ in range(6)]
number_values = [float(value) for value in values if float(value) > 0]
print('{} valores positivos'.format(len(number_values)))
print('{:.1f}'.format(sum(number_values)/len(number_values)))
