class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        v1_259 = {}
        v2_320 = -1
        for v3_881 in range(len(s)):
            v_junk_58 = 11
            if s[v3_881] not in v1_259:
                v1_259[s[v3_881]] = v3_881
            else:
                v2_320 = max(v2_320, v3_881 - v1_259[s[v3_881]] - 1)
        return v2_320