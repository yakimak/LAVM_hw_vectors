import numpy as np

def get_fire_directions(v, u):

    v = np.array(v, dtype=float)
    u = np.array(u, dtype=float)
    
    right = np.cross(v, u)
    left = -right
    
    return right, left

# Пример 1
right, left = get_fire_directions([1, 0, 0], [0, 1, 0])
print("Вправо:", right)    # [0. 0. 1.]
print("Влево:", left)      # [ 0.  0. -1.]

# Пример 1
right, left = get_fire_directions([2, 5, 0], [0, 0, 7])
print("Вправо:", right)    # [ 35. -14.   0.]
print("Влево:", left)      # [-35.  14.  0.]

