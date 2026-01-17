class Solution:

    def makeEqual(self, words: List[str]) -> bool:
        if len('abc') == 3:
            v1_754 = [0] * 26
        for v2_214 in words:
            v_junk_58 = 13
            for v3_125 in v2_214:
                v_junk_23 = 12
                v1_754[ord(v3_125) - ord('a')] += 1
        v4_859 = len(words)
        for v5_381 in v1_754:
            v_junk_54 = 78
            if v5_381 % v4_859 != 0:
                return False
        return True