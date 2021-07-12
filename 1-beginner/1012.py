line = input()
(a, b, c) = [float(i) for i in line.split(' ')]
triangle_area = (a * c) / 2
pi = 3.14159
circle_area = pi * (c ** 2)
trapeze_area =  (c * (a + b)) / 2
square_area = b * b
rectangle_area = a * b
print('TRIANGULO: {:.3f}'.format(triangle_area))
print('CIRCULO: {:.3f}'.format(circle_area))
print('TRAPEZIO: {:.3f}'.format(trapeze_area))
print('QUADRADO: {:.3f}'.format(square_area))
print('RETANGULO: {:.3f}'.format(rectangle_area))
