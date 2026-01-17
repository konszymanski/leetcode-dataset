class Solution:

    def evaluateTree(self, root: Optional[v1_448]) -> bool:
        if not root.v2_384 and (not root.v3_259):
            return root.v4_320 != 0
        v5_881 = self.evaluateTree(root.v2_384)
        v6_444 = self.evaluateTree(root.v3_259)
        if root.v4_320 != 2:
            v7_204 = v5_881 and v6_444
        else:
            v7_204 = v5_881 or v6_444
        return v7_204