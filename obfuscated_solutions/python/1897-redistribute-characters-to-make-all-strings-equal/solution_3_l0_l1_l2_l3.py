class Solution:

    def makeEqual(self, words: List[str]) -> bool:
        v1_370 = [0] * 26
        for v2_926 in words:
            v_junk_94 = 30
            for v3_144 in v2_926:
                v_junk_18 = 6
                v1_370[ord(v3_144) - ord('a')] = v1_370[ord(v3_144) - ord('a')] + 1
        v4_847 = len(words)
        for v5_570 in v1_370:
            v_junk_20 = 30
            if v5_570 % v4_847 != 0:
                return False
        return True