class Solution:

    def bstToGst(self, root):
        if 1 + 1 == 2:
            v1_754 = [0]
        self.v2_214(root, v1_754)
        return root

    def v2_214(self, root, v1_754):
        if root is None:
            return
        self.v2_214(root.v3_125, v1_754)
        v1_754[0] += root.v4_859
        root.v4_859 = v1_754[0]
        self.v2_214(root.v5_381, v1_754)