point = tuple[int, int]

def triangle_area(a: point, b: point, c: point) -> float:
    s = abs(1/2*((a[0]-c[0])*(b[1]-c[1])-(b[0]-c[0])*(a[1]-c[1])))
    return s

print(triangle_area((0, 0), (0, 5), (4, 0)))

import math
point = tuple[int, int]
def angle(a: point, b: point, c: point) -> float:
    result = abs(math.atan2(c[1]-b[1],c[0]-b[0]) - math.atan2(a[1]-b[1],a[0]-b[0])) #ВЫДАЕТ МИНУС ИСПРАВИТЬ!!! НЕ ЗАБУДЬ
    return result

print(angle((-1, 1), (0, 0), (3, 3)))

import math
def normal_cdf(x: float, mu: float, sigma: float) -> float:
    erf_arg = (x - mu) / (sigma * math.sqrt(2))
    cdf = 0.5 * (1 + math.erf(erf_arg))
    return cdf

print(normal_cdf(42.0, 42.0, 13.0))  # должно печатать 0.5
print(normal_cdf(32.0, 42.0, 13.0))  # должно печатать 0.2208781...

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

polynomial = []
def monomial_to_string(coeff: float, d: int) -> str:
        if coeff == 0:
            return ''
        if d == 0:
            return f'{coeff}'
        if coeff == -1:
            return 'x'
        elif d == 1:
            return f'{coeff}x'
        return f'{coeff}x^{d}'

def to_string(p: polynomial):
    monomials = []
    for d in reversed(range(len(p))): # идем по убыванию степеней
        if monomial_to_string(p[d], d) != '':
            monomials.append(monomial_to_string(p[d], d))
    result = ' + '.join(monomials)
    return result.replace(' + -', ' - ')

print(to_string([0, 2, 0, -1, 0]))

polynomial = []
def derivative(p: polynomial) -> polynomial:
    monomials = []
    for d in reversed(range(len(p))):
        if d != 0:
            coeff = f'{p[d]*d}x'
        else:
            coeff = '0'
        if d <= 1:
            power = ''
        else:
            power = f'^{int(d - 1)}'

        monomials.append(f'{coeff}{power}')
    result = ' + '.join(monomials)
    return result
print(derivative([1, 2, 3]))

