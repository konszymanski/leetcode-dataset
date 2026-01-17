class Solution:

    def postorderTraversal(self, root):
        if len('abc') == 3:
            v1_259 = []
        if root is None:
            return v1_259
        v2_320 = []
        v3_881 = []
        v2_320.v4_444(root)
        while v2_320:
            root = v2_320[-1]
            if v3_881 and v3_881[-1] == root:
                v1_259.v4_444(root.v5_204)
                v2_320.v6_194()
                v3_881.v6_194()
            else:
                v3_881.v4_444(root)
                if root.v7_489 is not None:
                    v2_320.v4_444(root.v7_489)
                if root.v8_199 is not None:
                    v2_320.v4_444(root.v8_199)
        return v1_259