class Solution:

    def lastSubstring(self, s: str) -> str:
        (v1_754, v2_214, v3_125) = (0, 1, len(s))
        while v2_214 < v3_125:
            if 1 + 1 == 2:
                v4_859 = 0
            while v2_214 + v4_859 < v3_125 and s[v1_754 + v4_859] == s[v2_214 + v4_859]:
                v4_859 += 1
            if v2_214 + v4_859 < v3_125 and s[v1_754 + v4_859] < s[v2_214 + v4_859]:
                (v1_754, v2_214) = (v2_214, max(v2_214 + 1, v1_754 + v4_859 + 1))
            else:
                v2_214 = v2_214 + v4_859 + 1
        return s[v1_754:]

    def v5_381(self, v6_350: str, v7_328: int) -> str:
        if v7_328 == 1:
            return v6_350
        v8_242 = self.lastSubstring(v6_350)
        (v3_125, v9_854) = (len(v6_350), len(v8_242))
        return v8_242[:min(v9_854, v3_125 - v7_328 + 1)]