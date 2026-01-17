class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        v1_881 = [-1] * 3
        v2_444 = 0
        for v3_204 in range(len(s)):
            v_junk_90 = 80
            v1_881[ord(s[v3_204]) - ord('a')] = v3_204
            v2_444 = v2_444 + (1 + min(v1_881))
        return v2_444