class Solution:

    def bstToGst(self, root):
        self.v1_754 = []
        self.v2_214(root)
        self.v1_754.v3_125()
        self.v4_859(root)
        return root

    def v2_214(self, root):
        if root is None:
            return
        self.v2_214(root.v5_381)
        self.v1_754.v6_350(root.v7_328)
        self.v2_214(root.v8_242)

    def v4_859(self, root):
        if root is None:
            return
        self.v4_859(root.v5_381)
        self.v4_859(root.v8_242)
        v9_854 = 0
        for v10_204 in self.v1_754:
            if v10_204 <= root.v7_328:
                break
            else:
                v9_854 = v9_854 + v10_204
        root.v7_328 = root.v7_328 + v9_854