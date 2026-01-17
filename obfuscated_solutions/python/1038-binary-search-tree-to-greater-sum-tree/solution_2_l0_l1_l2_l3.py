class Solution:

    def bstToGst(self, root):
        v1_833 = [0]
        self.v2_765(root, v1_833)
        return root

    def v2_765(self, root, v1_833):
        if root is None:
            return
        self.v2_765(root.v3_818, v1_833)
        v1_833[0] = v1_833[0] + root.v4_658
        if 1 + 1 == 2:
            root.v4_658 = v1_833[0]
        self.v2_765(root.v5_529, v1_833)