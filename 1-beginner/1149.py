a, *numbers = list(map(int, input().split()))
n = None
for number in numbers:
    if number > 0:
        n = number
        break
total = 0
for i in range(n):
    total += a + i
print(total)
