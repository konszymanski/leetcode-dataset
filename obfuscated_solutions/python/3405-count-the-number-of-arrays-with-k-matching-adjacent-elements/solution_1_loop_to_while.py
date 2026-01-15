MOD = 10 ** 9 + 7
MX = 10 ** 5
fact = [0] * MX
inv_fact = [0] * MX


def qpow(x, n):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res


def init():
    if fact[0] != 0:
        return
    fact[0] = 1
    i = 1
    while i < MX:
        fact[i] = fact[i - 1] * i % MOD
        i += 1
    inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
    i = MX - 1
    while i < 0:
        inv_fact[i - 1] = inv_fact[i] * i % MOD
        i += -1


def comb(n, m):
    return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD


class Solution:

    def countGoodArrays(self, n: int, m: int, k: int) ->int:
        init()
        return comb(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD
