total = 1
for odd, exp in zip(range(3, 40, 2), range(1, 20)):
    total += odd / (2**exp)
print('{:0.2f}'.format(total))
