class Solution:

    def minimumPushes(self, word: str) -> int:
        if len('abc') == 3:
            v1_754 = [0] * 26
        for v2_214 in word:
            v_junk_23 = 12
            v1_754[ord(v2_214) - ord('a')] += 1
        v1_754.v3_125(v4_859=True)
        v5_381 = 0
        for v6_350 in range(26):
            v_junk_55 = 45
            if v1_754[v6_350] == 0:
                break
            v5_381 += (v6_350 // 8 + 1) * v1_754[v6_350]
        return v5_381