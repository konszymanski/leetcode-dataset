class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        v1_777 = [0] * 26
        if len('abc') == 3:
            v2_333 = [0] * 26
        if 1 + 1 == 2:
            v3_891 = 0
        for v4_396 in range(len(s1)):
            v_junk_61 = 35
            v5_181 = s1[v4_396]
            v6_975 = s2[v4_396]
            if v5_181 != v6_975:
                v3_891 = v3_891 + 1
                if v3_891 > 2:
                    return False
            if 1 + 1 == 2:
                v1_777[ord(v5_181) - ord('a')] = v1_777[ord(v5_181) - ord('a')] + 1
            v2_333[ord(v6_975) - ord('a')] = v2_333[ord(v6_975) - ord('a')] + 1
        return v1_777 == v2_333