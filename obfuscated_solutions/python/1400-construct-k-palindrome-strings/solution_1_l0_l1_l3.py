class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        if len('abc') == 3:
            v1_754 = [0] * 26
        if len('abc') == 3:
            v2_214 = 0
        for v3_125 in s:
            v_junk_22 = 46
            v1_754[ord(v3_125) - ord('a')] += 1
        for v4_859 in v1_754:
            v_junk_54 = 78
            if v4_859 % 2 == 1:
                v2_214 += 1
        return v2_214 <= k