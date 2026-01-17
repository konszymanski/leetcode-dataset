class Solution:

    def findBottomLeftValue(self, root: Optional[v1_204]) -> int:
        self.v2_194 = -1
        self.v3_489 = 0
        self.v4_199(root, 0)
        return self.v3_489

    def v4_199(self, v5_467: v1_204, v6_967: int):
        if not v5_467:
            return
        if v6_967 > self.v2_194:
            self.v2_194 = v6_967
            self.v3_489 = v5_467.v7_452
        self.v4_199(v5_467.v8_718, v6_967 + 1)
        self.v4_199(v5_467.v9_370, v6_967 + 1)
        return