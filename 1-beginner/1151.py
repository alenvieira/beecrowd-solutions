n = int(input())
numbers = []
if n >= 1:
    numbers.append(0)
if n >= 2:
    numbers.append(1)
    for i in range(2, n):
        numbers.append(sum(numbers[-2:]))
print(*numbers)
