polynomial = list[float | int]
def calculate(p: polynomial, x: float) -> float:
    value = 0
    power_of_x = 1  # x^0
    for i, pi in enumerate(p):
        value += pi * power_of_x
        power_of_x *= x  # следующая степень x
    return value
print(calculate([1,2,3], 2.0))