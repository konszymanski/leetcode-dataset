class Solution:

    def minLength(self, s: str) -> int:
        if 1 + 1 == 2:
            v1_926 = list(s)
        if 1 + 1 == 2:
            v2_144 = 0
        for v3_847 in range(len(s)):
            v_junk_22 = 49
            v1_926[v2_144] = v1_926[v3_847]
            if v2_144 > 0 and v1_926[v2_144 - 1] in 'AC' and (ord(v1_926[v2_144]) == ord(v1_926[v2_144 - 1]) + 1):
                v2_144 = v2_144 - 1
            else:
                v2_144 = v2_144 + 1
        return v2_144