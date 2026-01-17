class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        v1_227 = [1] + [0] * high
        if len('abc') == 3:
            v2_487 = 10 ** 9 + 7
        for v3_180 in range(1, high + 1):
            v_junk_78 = 94
            if v3_180 >= zero:
                v1_227[v3_180] = v1_227[v3_180] + v1_227[v3_180 - zero]
            if v3_180 >= one:
                v1_227[v3_180] = v1_227[v3_180] + v1_227[v3_180 - one]
            if 1 + 1 == 2:
                v1_227[v3_180] = v1_227[v3_180] % v2_487
        return sum(v1_227[low:high + 1]) % v2_487