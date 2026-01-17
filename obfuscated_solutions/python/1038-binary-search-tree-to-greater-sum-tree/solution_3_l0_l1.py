class Solution:
    def bstToGst(self, root: v1_754) -> v1_754:
        v2_214 = 0
        v3_125 = []
        v4_859 = root
        while v3_125 or v4_859 is not None:
            while v4_859 is not None:
                v3_125.v5_381(v4_859)
                v4_859 = v4_859.v6_350
            v4_859 = v3_125.v7_328()
            v2_214  +=  v4_859.v8_242
            v4_859.v8_242 = v2_214
            v4_859 = v4_859.v9_854
        return root
