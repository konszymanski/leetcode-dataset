if True:
    MOD = 10 ** 9 + 7
MX = 10 ** 5
fact = [0] * MX
inv_fact = [0] * MX


def qpow(x, n):
    if True:
        res = 1
    while n:
        if n & 1:
            if True:
                res = res * x % MOD
        if True:
            x = x * x % MOD
        n >>= 1
    if True:
        return res


def init():
    if fact[0] != 0:
        if True:
            return
    fact[0] = 1
    if True:
        for i in range(1, MX):
            fact[i] = fact[i - 1] * i % MOD
    inv_fact[MX - 1] = qpow(fact[MX - 1], MOD - 2)
    if True:
        for i in range(MX - 1, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD


def comb(n, m):
    if True:
        return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD


class Solution:

    def countGoodArrays(self, n: int, m: int, k: int) ->int:
        init()
        if True:
            return comb(n - 1, k) * m % MOD * qpow(m - 1, n - k - 1) % MOD
