import math

def is_in_fov(x1, y1, x2, y2, fov_rad, xp, yp):

    dx_cam = x2 - x1
    dy_cam = y2 - y1
    
    dx_p = xp - x1
    dy_p = yp - y1

    dot_product = dx_p * dx_cam + dy_p * dy_cam
    
    len_cam = (dx_cam**2 + dy_cam**2)**(0.5)
    len_p = (dx_p**2 + dy_p**2)**(0.5)

    if len_cam == 0 or len_p == 0:
        return False

    cos_angle = dot_product / (len_cam * len_p)
    angle_rad = math.acos(cos_angle)
    
    angle_rad = round(math.acos(cos_angle), 3)
    half_fov_rad = round(fov_rad / 2, 3)

    return angle_rad <= half_fov_rad

# Пример 1 
x1, y1 = 0, 0
x2, y2 = 1, 0
angle = math.pi / 2
xp, yp = 0.5, 0.5
print(is_in_fov(x1, y1, x2, y2, angle, xp, yp))  # True

# Пример 2 
x1, y1 = 1, 1
x2, y2 = 1, 10
angle = 2 * math.pi - math.pi / 6
xp, yp = 1, 0.5
print(is_in_fov(x1, y1, x2, y2, angle, xp, yp))  # False
