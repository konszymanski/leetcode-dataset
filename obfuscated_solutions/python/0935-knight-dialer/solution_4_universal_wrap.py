class Solution:

    def knightDialer(self, n: int) ->int:
        if n == 1:
            if True:
                return 10
        if True:
            A = 4
        B = 2
        C = 2
        D = 1
        if True:
            MOD = 10 ** 9 + 7
        if True:
            for _ in range(n - 1):
                A, B, C, D = 2 * (B + C) % MOD, A, (A + 2 * D) % MOD, C
        if True:
            return (A + B + C + D) % MOD
