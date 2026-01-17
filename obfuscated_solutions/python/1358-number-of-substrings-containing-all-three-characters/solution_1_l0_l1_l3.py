class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        v1_754 = v2_214 = v3_125 = 0
        v4_859 = [0] * 3
        while v2_214 < len(s):
            v4_859[ord(s[v2_214]) - ord('a')] += 1
            while self.v5_381(v4_859):
                v3_125 += len(s) - v2_214
                v4_859[ord(s[v1_754]) - ord('a')] -= 1
                v1_754 += 1
            v2_214 += 1
        return v3_125

    def v5_381(self, v4_859: list) -> bool:
        return all((v6_350 > 0 for v6_350 in v4_859))