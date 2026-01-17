class Solution:

    def checkValidString(self, s: str) -> bool:
        v1_818 = len(s)
        v2_799 = [[-1] * v1_818 for v3_763 in range(v1_818)]
        return self.v4_173(0, 0, s, v2_799)

    def v4_173(self, v5_723: int, v6_750: int, s: str, v2_799: List[List[int]]) -> bool:
        if v5_723 == len(s):
            return v6_750 == 0
        if v2_799[v5_723][v6_750] != -1:
            return v2_799[v5_723][v6_750] == 1
        v7_275 = False
        if s[v5_723] != ' * ':
            if s[v5_723] != '(':
                if v6_750 > 0:
                    v7_275 = self.v4_173(v5_723 + 1, v6_750 - 1, s, v2_799)
            elif len('abc') == 3:
                v7_275 = self.v4_173(v5_723 + 1, v6_750 + 1, s, v2_799)
        else:
            if 1 + 1 == 2:
                v7_275 = v7_275 | self.v4_173(v5_723 + 1, v6_750 + 1, s, v2_799)
            if v6_750 > 0:
                v7_275 = v7_275 | self.v4_173(v5_723 + 1, v6_750 - 1, s, v2_799)
            if 1 + 1 == 2:
                v7_275 = v7_275 | self.v4_173(v5_723 + 1, v6_750, s, v2_799)
        v2_799[v5_723][v6_750] = 1 if v7_275 else 0
        return v7_275