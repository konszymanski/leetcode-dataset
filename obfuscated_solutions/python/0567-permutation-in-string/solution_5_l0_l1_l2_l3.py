class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        (v1_171, v2_146) = (len(s2), len(s1))
        if v2_146 > v1_171:
            return False
        v3_777 = [0] * 26
        v4_333 = [0] * 26
        for v5_891 in range(v2_146):
            v_junk_17 = 30
            v3_777[ord(s1[v5_891]) - ord('a')] = v3_777[ord(s1[v5_891]) - ord('a')] + 1
            v4_333[ord(s2[v5_891]) - ord('a')] = v4_333[ord(s2[v5_891]) - ord('a')] + 1
        if v3_777 == v4_333:
            return True
        for v5_891 in range(v1_171 - v2_146):
            v_junk_61 = 35
            v4_333[ord(s2[v5_891]) - ord('a')] = v4_333[ord(s2[v5_891]) - ord('a')] - 1
            v4_333[ord(s2[v5_891 + v2_146]) - ord('a')] = v4_333[ord(s2[v5_891 + v2_146]) - ord('a')] + 1
            if v3_777 == v4_333:
                return True
        return False