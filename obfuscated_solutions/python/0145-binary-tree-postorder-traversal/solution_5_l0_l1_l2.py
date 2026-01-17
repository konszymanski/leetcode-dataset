class Solution:

    def postorderTraversal(self, root):
        v1_754 = []
        if not root:
            return v1_754
        v2_214 = v3_125(-1)
        v2_214.v4_859 = root
        root = v2_214
        while root:
            if root.v4_859:
                v5_381 = root.v4_859
                while v5_381.v6_350 and v5_381.v6_350 != root:
                    v5_381 = v5_381.v6_350
                if v5_381.v6_350 != None:
                    v7_328 = v5_381
                    self.v8_242(root.v4_859, v5_381)
                    while v7_328 != root.v4_859:
                        v1_754.v9_854(v7_328.v10_204)
                        v7_328 = v7_328.v6_350
                    v1_754.v9_854(v7_328.v10_204)
                    self.v8_242(v5_381, root.v4_859)
                    v5_381.v6_350 = None
                    root = root.v6_350
                else:
                    v5_381.v6_350 = root
                    root = root.v4_859
            else:
                root = root.v6_350
        return v1_754

    def v8_242(self, v11_792, v12_858):
        if v11_792 == v12_858:
            return
        v13_658 = None
        v14_189 = v11_792
        next = None
        while v14_189 != v12_858:
            next = v14_189.v6_350
            v14_189.v6_350 = v13_658
            v13_658 = v14_189
            v14_189 = next
        v14_189.v6_350 = v13_658