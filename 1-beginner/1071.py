x = int(input())
y = int(input())
range_xy = range(x+1, y)
if (x > y):
    range_xy = range(y+1, x)
sum_xy = 0
for i in range_xy:
    if i % 2 != 0:
        sum_xy = sum_xy + i
print(sum_xy)
