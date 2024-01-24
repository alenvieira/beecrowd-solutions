number = int(input())
while number != 0:
    total = 0
    if number % 2 != 0:
        number += 1
    for i in range(number, number + 10, 2):
        total += i
    print(total)
    number = int(input())
