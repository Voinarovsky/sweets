import math

point = tuple[int, int]

def triangle_area(a: point, b: point, c: point) -> float:
    s = abs(1/2*((a[0]-c[0])*(b[1]-c[1])-(b[0]-c[0])*(a[1]-c[1])))
    return s

print(triangle_area((0, 0), (0, 5), (4, 0)))