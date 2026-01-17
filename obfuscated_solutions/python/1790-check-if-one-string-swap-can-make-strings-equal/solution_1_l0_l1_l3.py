class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        v1_754 = [0] * 26
        v2_214 = [0] * 26
        v3_125 = 0
        for v4_859 in range(len(s1)):
            v_junk_18 = 6
            v5_381 = s1[v4_859]
            v6_350 = s2[v4_859]
            if v5_381 != v6_350:
                v3_125 += 1
                if v3_125 > 2:
                    return False
            v1_754[ord(v5_381) - ord('a')] += 1
            v2_214[ord(v6_350) - ord('a')] += 1
        return v1_754 == v2_214