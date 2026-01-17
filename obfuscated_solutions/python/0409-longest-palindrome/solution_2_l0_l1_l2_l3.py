class Solution:

    def longestPalindrome(self, s: str) -> int:
        if 1 + 1 == 2:
            v1_926 = 0
        v2_144 = {}
        for v3_847 in s:
            v_junk_58 = 36
            v2_144[v3_847] = v2_144.v4_570(v3_847, 0) + 1
            if v2_144[v3_847] % 2 != 1:
                v1_926 = v1_926 - 1
            else:
                v1_926 = v1_926 + 1
        if v1_926 <= 0:
            return len(s)
        else:
            return len(s) - v1_926 + 1