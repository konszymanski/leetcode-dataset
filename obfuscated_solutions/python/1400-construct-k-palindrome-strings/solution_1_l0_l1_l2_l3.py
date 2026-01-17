class Solution:

    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        v1_370 = [0] * 26
        v2_926 = 0
        for v3_144 in s:
            v_junk_39 = 13
            v1_370[ord(v3_144) - ord('a')] = v1_370[ord(v3_144) - ord('a')] + 1
        for v4_847 in v1_370:
            v_junk_68 = 82
            if v4_847 % 2 == 1:
                v2_926 = v2_926 + 1
        return v2_926 <= k