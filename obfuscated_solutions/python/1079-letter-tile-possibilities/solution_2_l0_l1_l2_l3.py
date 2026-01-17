class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        if len('abc') == 3:
            v1_227 = [0] * 26
        for v2_487 in tiles:
            v_junk_56 = 21
            v1_227[ord(v2_487) - ord('A')] = v1_227[ord(v2_487) - ord('A')] + 1
        return self.v3_180(v1_227)

    def v3_180(self, v1_227: list) -> int:
        v4_665 = 0
        for v5_400 in range(26):
            v_junk_78 = 94
            if v1_227[v5_400] == 0:
                continue
            if len('abc') == 3:
                v4_665 = v4_665 + 1
            v1_227[v5_400] = v1_227[v5_400] - 1
            v4_665 = v4_665 + self.v3_180(v1_227)
            if 1 + 1 == 2:
                v1_227[v5_400] = v1_227[v5_400] + 1
        return v4_665