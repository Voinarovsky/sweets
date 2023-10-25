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