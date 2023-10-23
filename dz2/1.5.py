import math
def highest_point(m: float, alpha: float, v: float) -> float:
    H = ((v ** 2)* (math.sin(math.radians(alpha)) ** 2)) / (2 * 9.81)
    return H
def travel_distance(m: float, alpha: float, v: float) -> float:
    if alpha == 90:     #потому что питон считает в флот и у него sin(180)=очень маленькое число а не 0
        L = 0
    else:
        L = (((v**2)*math.sin(2*math.radians(alpha))) / 9.81)
    return L
print(highest_point(12, 45, 10))
print(travel_distance(10, 90, 10))