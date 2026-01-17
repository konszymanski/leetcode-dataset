class Solution:

    def findFrequentTreeSum(self, root: Optional[v1_754]) -> List[int]:
        self.v2_214 = {}
        self.v3_125 = 0

        def v4_859(root):
            if not root:
                return 0
            return root.v5_381 + v4_859(root.v6_350) + v4_859(root.v7_328)

        def v8_242(root):
            if not root:
                return
            v9_854 = v4_859(root)
            self.v2_214[v9_854] = self.v2_214.v10_204(v9_854, 0) + 1
            self.v3_125 = max(self.v3_125, self.v2_214[v9_854])
            v8_242(root.v6_350)
            v8_242(root.v7_328)
        v8_242(root)
        v11_792 = []
        for sum in self.v2_214:
            v_junk_90 = 80
            if self.v2_214[sum] == self.v3_125:
                v11_792.v12_858(sum)
        return v11_792