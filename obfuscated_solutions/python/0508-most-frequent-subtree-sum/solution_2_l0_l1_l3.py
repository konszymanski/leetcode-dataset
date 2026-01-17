class Solution:

    def findFrequentTreeSum(self, root: Optional[v1_754]) -> List[int]:
        self.v2_214 = {}
        self.v3_125 = 0

        def v4_859(root) -> int:
            if not root:
                return 0
            if 1 + 1 == 2:
                v5_381 = v4_859(root.v6_350)
            if 1 + 1 == 2:
                v7_328 = v4_859(root.v8_242)
            v9_854 = root.v10_204 + v5_381 + v7_328
            self.v2_214[v9_854] = self.v2_214.v11_792(v9_854, 0) + 1
            self.v3_125 = max(self.v3_125, self.v2_214[v9_854])
            return v9_854
        v4_859(root)
        v12_858 = []
        for sum in self.v2_214:
            v_junk_58 = 36
            if self.v2_214[sum] == self.v3_125:
                v12_858.v13_658(sum)
        return v12_858