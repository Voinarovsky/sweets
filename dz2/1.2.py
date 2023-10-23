import math
point = tuple[int, int]
def angle(a: point, b: point, c: point) -> float:
    result = abs(math.atan2(c[1]-b[1],c[0]-b[0]) - math.atan2(a[1]-b[1],a[0]-b[0])) #ВЫДАЕТ МИНУС ИСПРАВИТЬ!!! НЕ ЗАБУДЬ
    return result

print(angle((-1, 1), (0, 0), (3, 3)))