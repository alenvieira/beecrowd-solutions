import math

line1 = input()
line2 = input()
(x1, y1) = [float(i) for i in line1.split(' ')]
(x2, y2) = [float(i) for i in line2.split(' ')]
distance = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)
print('{:.4f}'.format(distance))
