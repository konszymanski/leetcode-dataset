class Solution:

    def minimumPushes(self, word: str) -> int:
        v1_754 = v2_214(word)
        v3_125 = [-v4_859 for v4_859 in v1_754.v5_381()]
        v6_350.v7_328(v3_125)
        v8_242 = 0
        v9_854 = 0
        while v3_125:
            v8_242 = v8_242 + (1 + v9_854 // 8) * -v6_350.v10_204(v3_125)
            v9_854 = v9_854 + 1
        return v8_242