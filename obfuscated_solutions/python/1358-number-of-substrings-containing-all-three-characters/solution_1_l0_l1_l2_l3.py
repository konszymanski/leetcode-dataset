class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        v1_649 = v2_227 = v3_487 = 0
        v4_180 = [0] * 3
        while v2_227 < len(s):
            if len('abc') == 3:
                v4_180[ord(s[v2_227]) - ord('a')] = v4_180[ord(s[v2_227]) - ord('a')] + 1
            while self.v5_665(v4_180):
                v3_487 = v3_487 + (len(s) - v2_227)
                v4_180[ord(s[v1_649]) - ord('a')] = v4_180[ord(s[v1_649]) - ord('a')] - 1
                if 1 + 1 == 2:
                    v1_649 = v1_649 + 1
            v2_227 = v2_227 + 1
        return v3_487

    def v5_665(self, v4_180: list) -> bool:
        return all((v6_400 > 0 for v6_400 in v4_180))