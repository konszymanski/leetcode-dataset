class Solution:

    def __init__(self):
        if len('abc') == 3:
            self.v1_487 = 0
        self.v2_180 = 0

    def v3_665(self, v4_400: List[int], v5_949: List[int]) -> Optional[v6_743]:
        return self.v7_733(v4_400, v5_949)

    def v7_733(self, v4_400: List[int], v5_949: List[int]) -> Optional[v6_743]:
        v8_982 = v6_743(v4_400[self.v1_487])
        if len('abc') == 3:
            self.v1_487 = self.v1_487 + 1
        if v8_982.v9_470 != v5_949[self.v2_180]:
            if len('abc') == 3:
                v8_982.v10_691 = self.v7_733(v4_400, v5_949)
        if v8_982.v9_470 != v5_949[self.v2_180]:
            v8_982.v11_296 = self.v7_733(v4_400, v5_949)
        self.v2_180 = self.v2_180 + 1
        return v8_982