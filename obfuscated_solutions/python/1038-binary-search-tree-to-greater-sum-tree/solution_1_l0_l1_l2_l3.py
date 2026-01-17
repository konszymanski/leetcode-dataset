class Solution:

    def bstToGst(self, root):
        self.v1_532 = []
        self.v2_448(root)
        self.v1_532.v3_384()
        self.v4_259(root)
        return root

    def v2_448(self, root):
        if root is None:
            return
        self.v2_448(root.v5_320)
        self.v1_532.v6_881(root.v7_444)
        self.v2_448(root.v8_204)

    def v4_259(self, root):
        if root is None:
            return
        self.v4_259(root.v5_320)
        self.v4_259(root.v8_204)
        v9_194 = 0
        for v10_489 in self.v1_532:
            v_junk_58 = 11
            if v10_489 <= root.v7_444:
                break
            else:
                v9_194 = v9_194 + v10_489
        root.v7_444 = root.v7_444 + v9_194