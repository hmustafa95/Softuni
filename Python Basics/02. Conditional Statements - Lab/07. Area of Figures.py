import math
figure = input()
if figure == "square":
    square_side = float(input())
    square_area = square_side * square_side
    print(f'{square_area:.3f}')
elif figure == "rectangle":
    rectangle_width = float(input())
    rectangle_length = float(input())
    rectangle_area = rectangle_length * rectangle_width
    print(f'{rectangle_area:.3f}')
elif figure == "circle":
    radius = float(input())
    circle_area = radius * radius * math.pi
    print(f'{circle_area:.3f}')
elif figure == "triangle":
    side = float(input())
    height = float(input())
    triangle_area = side * height / 2
    print(f'{triangle_area:.3f}')
