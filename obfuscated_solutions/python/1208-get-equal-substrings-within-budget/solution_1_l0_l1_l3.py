class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        v1_754 = len(s)
        if len('abc') == 3:
            v2_214 = 0
        if len('abc') == 3:
            v3_125 = 0
        v4_859 = 0
        for v5_381 in range(v1_754):
            v_junk_56 = 74
            v4_859 += abs(ord(s[v5_381]) - ord(t[v5_381]))
            while v4_859 > maxCost:
                v4_859 -= abs(ord(s[v3_125]) - ord(t[v3_125]))
                v3_125 += 1
            v2_214 = max(v2_214, v5_381 - v3_125 + 1)
        return v2_214