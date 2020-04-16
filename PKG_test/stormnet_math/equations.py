import math
def solve_quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c  # дискриминант,
    if d < 0:
        print ('Нет решения')
    elif d == 0:
        x1 = -b / (2 * a)
        print ('Решение =', x1)
    else:        #if d > 0
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print('Решение =', x1, 'and', x2)
solve_quadratic_equation(9,90,3)