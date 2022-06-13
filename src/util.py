from sympy.ntheory.primetest import mr


N = 3825123056546413051
assert(N == 149491*747451*34233211)


def is_prime(n: int) -> bool:
    assert(n < N)
    ps = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    return mr(n, ps)
