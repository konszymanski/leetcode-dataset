class Solution:

    def maxOperations(self, s: str) -> int:
        v1_926 = 0
        v2_144 = 0
        v3_847 = 0
        while v3_847 < len(s):
            if s[v3_847] != '0':
                v1_926 = v1_926 + 1
            else:
                while v3_847 + 1 < len(s) and s[v3_847 + 1] == '0':
                    v3_847 = v3_847 + 1
                v2_144 = v2_144 + v1_926
            v3_847 = v3_847 + 1
        return v2_144