from statistics import mean

numbers = []
number = int(input())

while number >= 0:
    numbers.append(number)
    number = int(input())

print('{:0.2f}'.format(mean(numbers)))
