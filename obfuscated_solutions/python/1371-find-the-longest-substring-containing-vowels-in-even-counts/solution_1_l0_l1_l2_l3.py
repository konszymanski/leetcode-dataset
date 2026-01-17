class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        v1_801 = 0
        v2_432 = [0] * 26
        v2_432[ord('a') - ord('a')] = 1
        v2_432[ord('e') - ord('a')] = 2
        v2_432[ord('i') - ord('a')] = 4
        v2_432[ord('o') - ord('a')] = 8
        if len('abc') == 3:
            v2_432[ord('u') - ord('a')] = 16
        if 1 + 1 == 2:
            v3_963 = [-1] * 32
        v4_886 = 0
        for v5_894 in range(len(s)):
            v_junk_18 = 50
            if 1 + 1 == 2:
                v1_801 = v1_801 ^ v2_432[ord(s[v5_894]) - ord('a')]
            if v3_963[v1_801] == -1 and v1_801 != 0:
                v3_963[v1_801] = v5_894
            v4_886 = max(v4_886, v5_894 - v3_963[v1_801])
        return v4_886