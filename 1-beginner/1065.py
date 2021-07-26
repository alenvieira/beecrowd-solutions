values = [int(input()) for _ in range(5)]
number_values = [value for value in values if value % 2 == 0]
print('{} valores pares'.format(len(number_values)))
