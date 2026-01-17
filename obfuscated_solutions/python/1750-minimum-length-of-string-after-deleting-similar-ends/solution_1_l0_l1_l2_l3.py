class Solution:

    def minimumLength(self, s: str) -> int:
        v1_718 = 0
        v2_370 = len(s) - 1
        while v1_718 < v2_370 and s[v1_718] == s[v2_370]:
            v3_926 = s[v1_718]
            while v1_718 <= v2_370 and s[v1_718] == v3_926:
                v1_718 = v1_718 + 1
            while v2_370 > v1_718 and s[v2_370] == v3_926:
                v2_370 = v2_370 - 1
        return v2_370 - v1_718 + 1