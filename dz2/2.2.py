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