values = [int(input()) for _ in range(5)]
number_even = [value for value in values if value % 2 == 0]
number_odd = [value for value in values if value % 2 != 0]
number_positives = [value for value in values if value > 0]
number_negatives = [value for value in values if value < 0]
print('{} valor(es) par(es)'.format(len(number_even)))
print('{} valor(es) impar(es)'.format(len(number_odd)))
print('{} valor(es) positivo(s)'.format(len(number_positives)))
print('{} valor(es) negativo(s)'.format(len(number_negatives)))
