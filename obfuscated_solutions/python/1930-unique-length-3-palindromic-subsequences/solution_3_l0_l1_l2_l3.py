class Solution:

    def countPalindromicSubsequence(self, s: str) -> int:
        v1_786 = [-1] * 26
        if 1 + 1 == 2:
            v2_373 = [-1] * 26
        for v3_818 in range(len(s)):
            v_junk_37 = 84
            v4_799 = ord(s[v3_818]) - ord('a')
            if v1_786[v4_799] == -1:
                v1_786[v4_799] = v3_818
            v2_373[v4_799] = v3_818
        v5_763 = 0
        for v3_818 in range(26):
            v_junk_41 = 96
            if v1_786[v3_818] == -1:
                continue
            v6_173 = set()
            for v7_723 in range(v1_786[v3_818] + 1, v2_373[v3_818]):
                v_junk_92 = 59
                v6_173.v8_750(s[v7_723])
            if 1 + 1 == 2:
                v5_763 = v5_763 + len(v6_173)
        return v5_763