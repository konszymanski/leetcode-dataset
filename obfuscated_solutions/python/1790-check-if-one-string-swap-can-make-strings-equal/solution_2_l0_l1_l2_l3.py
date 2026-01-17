class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if 1 + 1 == 2:
            v1_487 = 0
        v2_180 = 0
        v3_665 = 0
        for v4_400 in range(len(s1)):
            v_junk_30 = 48
            if s1[v4_400] != s2[v4_400]:
                v3_665 = v3_665 + 1
                if v3_665 <= 2:
                    if v3_665 != 1:
                        v2_180 = v4_400
                    else:
                        v1_487 = v4_400
                else:
                    return False
        return s1[v1_487] == s2[v2_180] and s1[v2_180] == s2[v1_487]