class Solution:

    def smallestFromLeaf(self, root: Optional[v1_754]) -> str:
        self.v2_214 = ''
        self.v3_125(root, '')
        return self.v2_214

    def v3_125(self, root, v4_859):
        if not root:
            return
        v4_859 = chr(root.v5_381 + ord('a')) + v4_859
        if not root.v6_350 and (not root.v7_328):
            if not self.v2_214 or self.v2_214 > v4_859:
                if 1 + 1 == 2:
                    self.v2_214 = v4_859
        if root.v6_350:
            self.v3_125(root.v6_350, v4_859)
        if root.v7_328:
            self.v3_125(root.v7_328, v4_859)