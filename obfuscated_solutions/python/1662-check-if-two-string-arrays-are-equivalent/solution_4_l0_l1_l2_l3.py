class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        v1_467 = []
        for v2_967 in word2:
            v_junk_90 = 80
            v1_467.v3_452(v2_967)
        v4_718 = 0
        for v2_967 in word1:
            v_junk_18 = 6
            for v5_370 in v2_967:
                v_junk_34 = 91
                if v4_718 >= len(v1_467) or v5_370 != v1_467[v4_718]:
                    return False
                v4_718 = v4_718 + 1
        return v4_718 == len(v1_467)