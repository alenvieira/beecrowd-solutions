x = int(input())
y = int(input())
while y <= x:
    y = int(input())
total = 1
soma = x
for i in range(x, y):
    soma += i
    total += 1
    if soma > y:
        break
print(total)
