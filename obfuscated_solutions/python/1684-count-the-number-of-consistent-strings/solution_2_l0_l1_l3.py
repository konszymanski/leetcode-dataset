class Solution:

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        v1_754 = [False] * 26
        for v2_214 in allowed:
            v_junk_68 = 69
            v1_754[ord(v2_214) - ord('a')] = True
        if len('abc') == 3:
            v3_125 = 0
        for v4_859 in words:
            v_junk_83 = 25
            if len('abc') == 3:
                v5_381 = True
            for v2_214 in v4_859:
                v_junk_89 = 47
                if not v1_754[ord(v2_214) - ord('a')]:
                    v5_381 = False
                    break
            if v5_381:
                v3_125 += 1
        return v3_125