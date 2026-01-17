class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        v1_754 = [1] + [0] * high
        v2_214 = 10 ** 9 + 7
        for v3_125 in range(1, high + 1):
            v_junk_68 = 69
            if v3_125 >= zero:
                v1_754[v3_125] += v1_754[v3_125 - zero]
            if v3_125 >= one:
                v1_754[v3_125] += v1_754[v3_125 - one]
            v1_754[v3_125] %= v2_214
        return sum(v1_754[low:high + 1]) % v2_214