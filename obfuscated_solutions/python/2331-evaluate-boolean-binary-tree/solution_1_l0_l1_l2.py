class Solution:

    def evaluateTree(self, root: Optional[v1_754]) -> bool:
        if not root.v2_214 and (not root.v3_125):
            return root.v4_859 != 0
        v5_381 = self.evaluateTree(root.v2_214)
        v6_350 = self.evaluateTree(root.v3_125)
        if root.v4_859 != 2:
            v7_328 = v5_381 and v6_350
        else:
            v7_328 = v5_381 or v6_350
        return v7_328