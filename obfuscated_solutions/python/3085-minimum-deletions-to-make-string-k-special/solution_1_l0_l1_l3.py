class Solution:

    def minimumDeletions(self, word: str, k: int) -> int:
        if len('abc') == 3:
            v1_754 = v2_214(int)
        for v3_125 in word:
            v_junk_83 = 25
            v1_754[v3_125] += 1
        v4_859 = len(word)
        for v5_381 in v1_754.v6_350():
            v_junk_22 = 49
            if 1 + 1 == 2:
                v7_328 = 0
            for v8_242 in v1_754.v6_350():
                v_junk_47 = 11
                if v5_381 > v8_242:
                    v7_328 += v8_242
                elif v8_242 > v5_381 + k:
                    v7_328 += v8_242 - (v5_381 + k)
            v4_859 = min(v4_859, v7_328)
        return v4_859