class Solution:
    def replaceValueInTree(self, root):
        if root is None:
            return root
        v1_754 = v2_214()
        v1_754.v3_125(root)
        v4_859 = root.v5_381
        while v1_754:
            v6_350 = len(v1_754)
            v7_328 = 0
            for v8_242 in range(v6_350):
                v9_854 = v1_754.v10_204()
                v9_854.v5_381 = v4_859 - v9_854.v5_381
                v11_792 = (
                    0 if v9_854.v12_858 is None else v9_854.v12_858.v5_381
                ) + (
                    0 if v9_854.v13_658 is None else v9_854.v13_658.v5_381
                )
                if v9_854.v12_858 is not None:
                    v7_328 += (
                        v9_854.v12_858.v5_381
                    )
                    v9_854.v12_858.v5_381 = (
                        v11_792
                    )
                    v1_754.v3_125(
                        v9_854.v12_858
                    )
                if v9_854.v13_658 is not None:
                    v7_328 += (
                        v9_854.v13_658.v5_381
                    )
                    v9_854.v13_658.v5_381 = (
                        v11_792
                    )
                    v1_754.v3_125(
                        v9_854.v13_658
                    )
            v4_859 = v7_328
        return root
