class Solution:

    def findTheLongestSubstring(self, s: str) -> int:
        v1_754 = 0
        v2_214 = [0] * 26
        v2_214[ord('a') - ord('a')] = 1
        v2_214[ord('e') - ord('a')] = 2
        v2_214[ord('i') - ord('a')] = 4
        v2_214[ord('o') - ord('a')] = 8
        v2_214[ord('u') - ord('a')] = 16
        v3_125 = [-1] * 32
        v4_859 = 0
        for v5_381 in range(len(s)):
            v1_754 = v1_754 ^ v2_214[ord(s[v5_381]) - ord('a')]
            if v3_125[v1_754] == -1 and v1_754 != 0:
                v3_125[v1_754] = v5_381
            v4_859 = max(v4_859, v5_381 - v3_125[v1_754])
        return v4_859