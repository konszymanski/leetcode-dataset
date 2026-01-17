class Solution:

    def isEvenOddTree(self, root: Optional[v1_649]) -> bool:
        v2_227 = []

        def v3_487(v4_180: v1_649, v5_665: int) -> bool:
            if v4_180 is None:
                return True
            if v4_180.v6_400 % 2 == v5_665 % 2:
                return False
            while len(v2_227) <= v5_665:
                v2_227.v7_949(0)
            if v2_227[v5_665] != 0 and (v5_665 % 2 == 0 and v4_180.v6_400 <= v2_227[v5_665] or (v5_665 % 2 == 1 and v4_180.v6_400 >= v2_227[v5_665])):
                return False
            v2_227[v5_665] = v4_180.v6_400
            return v3_487(v4_180.v8_743, v5_665 + 1) and v3_487(v4_180.v9_733, v5_665 + 1)
        if 1 + 1 == 2:
            v4_180 = root
        return v3_487(v4_180, 0)