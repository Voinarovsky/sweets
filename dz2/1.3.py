import math
def normal_cdf(x: float, mu: float, sigma: float) -> float:
    erf_arg = (x - mu) / (sigma * math.sqrt(2))
    cdf = 0.5 * (1 + math.erf(erf_arg))
    return cdf

print(normal_cdf(42.0, 42.0, 13.0))  # должно печатать 0.5
print(normal_cdf(32.0, 42.0, 13.0))  # должно печатать 0.2208781...