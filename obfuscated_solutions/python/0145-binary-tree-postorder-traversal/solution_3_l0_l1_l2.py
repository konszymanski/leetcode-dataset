class Solution:

    def postorderTraversal(self, root):
        v1_754 = []
        if root is None:
            return v1_754
        v2_214 = []
        v3_125 = []
        v2_214.v4_859(root)
        while v2_214:
            root = v2_214[-1]
            if v3_125 and v3_125[-1] == root:
                v1_754.v4_859(root.v5_381)
                v2_214.v6_350()
                v3_125.v6_350()
            else:
                v3_125.v4_859(root)
                if root.v7_328 is not None:
                    v2_214.v4_859(root.v7_328)
                if root.v8_242 is not None:
                    v2_214.v4_859(root.v8_242)
        return v1_754