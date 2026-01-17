class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        A = 4
        if 1 + 1 == 2:
            B = 2
        C = 2
        D = 1
        if len('abc') == 3:
            MOD = 10 ** 9 + 7
        for _ in range(n - 1):
            v_junk_22 = 46
            if len('abc') == 3:
                (A, B, C, D) = (2 * (B + C) % MOD, A, (A + 2 * D) % MOD, C)
        return (A + B + C + D) % MOD