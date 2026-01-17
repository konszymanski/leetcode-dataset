class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        v1_754 = [1] + [-1] * high
        v2_214 = 10 ** 9 + 7

        def v3_125(v4_859):
            if v1_754[v4_859] != -1:
                return v1_754[v4_859]
            v5_381 = 0
            if v4_859 >= zero:
                v5_381 = v5_381 + v3_125(v4_859 - zero)
            if v4_859 >= one:
                v5_381 = v5_381 + v3_125(v4_859 - one)
            v1_754[v4_859] = v5_381 % v2_214
            return v1_754[v4_859]
        return sum((v3_125(v4_859) for v4_859 in range(low, high + 1))) % v2_214