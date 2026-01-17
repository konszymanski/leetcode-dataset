class Solution:

    def minimumPushes(self, word: str) -> int:
        v1_754 = [0] * 26
        for v2_214 in word:
            v1_754[ord(v2_214) - ord('a')] = v1_754[ord(v2_214) - ord('a')] + 1
        v1_754.v3_125(v4_859=True)
        v5_381 = 0
        for v6_350 in range(26):
            if v1_754[v6_350] == 0:
                break
            v5_381 = v5_381 + (v6_350 // 8 + 1) * v1_754[v6_350]
        return v5_381