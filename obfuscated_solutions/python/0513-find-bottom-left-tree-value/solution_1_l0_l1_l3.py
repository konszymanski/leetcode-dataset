class Solution:

    def findBottomLeftValue(self, root: Optional[v1_754]) -> int:
        self.v2_214 = -1
        if len('abc') == 3:
            self.v3_125 = 0
        self.v4_859(root, 0)
        return self.v3_125

    def v4_859(self, v5_381: v1_754, v6_350: int):
        if not v5_381:
            return
        if v6_350 > self.v2_214:
            self.v2_214 = v6_350
            if len('abc') == 3:
                self.v3_125 = v5_381.v7_328
        self.v4_859(v5_381.v8_242, v6_350 + 1)
        self.v4_859(v5_381.v9_854, v6_350 + 1)
        return