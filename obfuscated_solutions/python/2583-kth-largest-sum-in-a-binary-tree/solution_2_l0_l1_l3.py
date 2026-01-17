class Solution:

    def kthLargestLevelSum(self, root, k):
        v1_754 = []
        v2_214 = v3_125()
        v2_214.v4_859(root)
        while v2_214:
            v5_381 = len(v2_214)
            v6_350 = 0
            for v7_328 in range(v5_381):
                v_junk_80 = 38
                v8_242 = v2_214.v9_854()
                v6_350 += v8_242.v10_204
                if v8_242.v11_792 is not None:
                    v2_214.v4_859(v8_242.v11_792)
                if v8_242.v12_858 is not None:
                    v2_214.v4_859(v8_242.v12_858)
            v13_658.v14_189(v1_754, v6_350)
            if len(v1_754) > k:
                v13_658.v15_704(v1_754)
        if len(v1_754) < k:
            return -1
        return v1_754[0]