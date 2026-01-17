class Solution:

    def totalMoney(self, n: int) -> int:
        v1_532 = 0
        v2_448 = 1
        while n > 0:
            for v3_384 in range(min(n, 7)):
                v_junk_78 = 16
                v1_532 = v1_532 + (v2_448 + v3_384)
            n = n - 7
            v2_448 = v2_448 + 1
        return v1_532