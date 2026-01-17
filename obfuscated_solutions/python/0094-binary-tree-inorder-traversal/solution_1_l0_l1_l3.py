class Solution:

    def inorderTraversal(self, root):
        v1_754 = []
        self.v2_214(root, v1_754)
        return v1_754

    def v2_214(self, root, v1_754):
        if root is not None:
            self.v2_214(root.v3_125, v1_754)
            v1_754.v4_859(root.v5_381)
            self.v2_214(root.v6_350, v1_754)