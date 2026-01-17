class Solution:

    def minimumLength(self, s: str) -> int:
        return self.v1_754(s, 0, len(s) - 1)

    def v1_754(self, s: str, v2_214: int, v3_125: int) -> int:
        if v2_214 >= v3_125 or s[v2_214] != s[v3_125]:
            return v3_125 - v2_214 + 1
        else:
            v4_859 = s[v2_214]
            while v2_214 <= v3_125 and s[v2_214] == v4_859:
                v2_214 += 1
            while v3_125 > v2_214 and s[v3_125] == v4_859:
                v3_125 -= 1
            return self.v1_754(s, v2_214, v3_125)