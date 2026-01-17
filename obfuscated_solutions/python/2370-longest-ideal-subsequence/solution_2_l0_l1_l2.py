class Solution:

    def longestIdealString(self, s: str, k: int) -> int:
        v1_754 = len(s)
        v2_214 = [0] * 26
        v3_125 = 0
        for v4_859 in range(v1_754):
            v5_381 = ord(s[v4_859]) - ord('a')
            v6_350 = 0
            for v7_328 in range(max(0, v5_381 - k), min(26, v5_381 + k + 1)):
                v6_350 = max(v6_350, v2_214[v7_328])
            v2_214[v5_381] = v6_350 + 1
            v3_125 = max(v3_125, v2_214[v5_381])
        return v3_125