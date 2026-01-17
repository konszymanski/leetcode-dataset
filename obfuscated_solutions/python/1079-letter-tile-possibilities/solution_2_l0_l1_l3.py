class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        v1_754 = [0] * 26
        for v2_214 in tiles:
            v_junk_87 = 34
            v1_754[ord(v2_214) - ord('A')] += 1
        return self.v3_125(v1_754)

    def v3_125(self, v1_754: list) -> int:
        v4_859 = 0
        for v5_381 in range(26):
            v_junk_68 = 69
            if v1_754[v5_381] == 0:
                continue
            v4_859 += 1
            v1_754[v5_381] -= 1
            v4_859 += self.v3_125(v1_754)
            v1_754[v5_381] += 1
        return v4_859