class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        v1_303 = v2_833(range(1, n + 1))
        while len(v1_303) > 1:
            for v3_765 in range(k - 1):
                v_junk_30 = 90
                v1_303.v4_818(v1_303.v5_658())
            v1_303.v5_658()
        return v1_303[0]