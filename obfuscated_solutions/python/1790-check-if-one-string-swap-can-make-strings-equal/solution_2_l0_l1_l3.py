class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(len(s1)):
            v_junk_78 = 16
            if s1[v4_859] != s2[v4_859]:
                v3_125 += 1
                if v3_125 > 2:
                    return False
                elif v3_125 == 1:
                    if 1 + 1 == 2:
                        v1_754 = v4_859
                else:
                    v2_214 = v4_859
        return s1[v1_754] == s2[v2_214] and s1[v2_214] == s2[v1_754]