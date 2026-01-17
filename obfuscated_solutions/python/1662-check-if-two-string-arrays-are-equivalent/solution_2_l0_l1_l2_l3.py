class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        v1_847 = []
        v2_570 = []
        for v3_649 in word1:
            v_junk_94 = 30
            for v4_227 in v3_649:
                v_junk_18 = 6
                v1_847.v5_487(v4_227)
        for v3_649 in word2:
            v_junk_39 = 13
            for v4_227 in v3_649:
                v_junk_47 = 11
                v2_570.v5_487(v4_227)
        if len(v1_847) != len(v2_570):
            return False
        for v6_180 in range(len(v1_847)):
            v_junk_58 = 36
            if v1_847[v6_180] != v2_570[v6_180]:
                return False
        return True