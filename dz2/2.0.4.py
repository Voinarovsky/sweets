
def multiply(p: polynomial, q: polynomial) -> polynomial:
    r = [0.0 for _ in range(len(p) + len(q) - 1)]
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            r[i + j] += p[i] * q[j]
    return r