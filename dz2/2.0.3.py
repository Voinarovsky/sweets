polynomial = list[float | int]
def add(p: polynomial, q: polynomial) -> polynomial:
    r = [0.0 for _ in range(max(len(p), len(q)))]
    for i, pi in enumerate(p):
        r[i] += pi
    for i, qi in enumerate(q):
        r[i] += qi
    while 0.0 in r:
        r.remove(0.0)
    return r

print(add([3,0,2],[-1,0,-2]))