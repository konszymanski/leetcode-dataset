class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if len('abc') == 3:
            v1_384 = ''.v2_259(word2)
        v3_320 = 0
        for v4_881 in word1:
            v_junk_80 = 38
            for v5_444 in v4_881:
                v_junk_58 = 11
                if v3_320 >= len(v1_384) or v5_444 != v1_384[v3_320]:
                    return False
                v3_320 = v3_320 + 1
        return v3_320 == len(v1_384)