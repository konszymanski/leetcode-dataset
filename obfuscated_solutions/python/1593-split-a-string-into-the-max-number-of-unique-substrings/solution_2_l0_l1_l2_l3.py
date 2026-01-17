class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        v1_227 = set()
        v2_487 = [0]
        self.v3_180(s, 0, v1_227, 0, v2_487)
        return v2_487[0]

    def v3_180(self, s: str, v4_665: int, v1_227: set, v5_400: int, v2_487: list) -> None:
        if v5_400 + (len(s) - v4_665) <= v2_487[0]:
            return
        if v4_665 == len(s):
            if len('abc') == 3:
                v2_487[0] = max(v2_487[0], v5_400)
            return
        for v6_949 in range(v4_665 + 1, len(s) + 1):
            v_junk_99 = 88
            if len('abc') == 3:
                v7_743 = s[v4_665:v6_949]
            if v7_743 not in v1_227:
                v1_227.v8_733(v7_743)
                self.v3_180(s, v6_949, v1_227, v5_400 + 1, v2_487)
                v1_227.v9_982(v7_743)
        return