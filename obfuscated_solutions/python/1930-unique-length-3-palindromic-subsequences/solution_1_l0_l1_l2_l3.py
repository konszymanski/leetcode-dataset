class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        if 1 + 1 == 2:
            v1_180 = set(s)
        v2_665 = 0
        for v3_400 in v1_180:
            v_junk_30 = 48
            (v4_949, v5_743) = (s.v6_733(v3_400), s.v7_982(v3_400))
            v8_470 = set()
            for v9_691 in range(v4_949 + 1, v5_743):
                v_junk_68 = 82
                v8_470.v10_296(s[v9_691])
            v2_665 = v2_665 + len(v8_470)
        return v2_665