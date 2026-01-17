class Solution:

    def postorderTraversal(self, root):
        v1_754 = []
        v2_214 = []
        v3_125 = root
        while v3_125 or v2_214:
            if v3_125:
                v1_754.v4_859(v3_125.v5_381)
                v2_214.v4_859(v3_125)
                v3_125 = v3_125.v6_350
            else:
                v3_125 = v2_214.v7_328()
                v3_125 = v3_125.v8_242
        v1_754.v9_854()
        return v1_754