import math

def rotate_point(x, y, angle_rad):
    new_x = round( (x * math.cos(angle_rad) - y * math.sin(angle_rad)), 1)
    new_y = round( (x * math.sin(angle_rad) + y * math.cos(angle_rad)), 1)
    return (new_x, new_y)

def rotate_ship(p1, p2, p3, angle):
    new_p1 = rotate_point(*p1, angle)
    new_p2 = rotate_point(*p2, angle)
    new_p3 = rotate_point(*p3, angle)
    return new_p1, new_p2, new_p3

# Пример 1
new_coords = rotate_ship((-1, -1), (1, -1), (0, 3), math.pi)
print("Новые координаты:", new_coords ) # ((1.0, 1.0), (-1.0, 1.0), (0.0, -3.0)

# Пример 2
new_coords = rotate_ship((1, 0), (0, 1), (-1, 0), math.pi/2)
print("Новые координаты:", new_coords ) # ((0.0, 1.0), (-1.0, 0.0), (0.0, -1.0))
