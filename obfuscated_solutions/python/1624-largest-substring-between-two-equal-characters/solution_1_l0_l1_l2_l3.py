class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        v1_384 = -1
        for v2_259 in range(len(s)):
            v_junk_58 = 11
            for v3_320 in range(v2_259 + 1, len(s)):
                v_junk_78 = 16
                if s[v2_259] == s[v3_320]:
                    v1_384 = max(v1_384, v3_320 - v2_259 - 1)
        return v1_384