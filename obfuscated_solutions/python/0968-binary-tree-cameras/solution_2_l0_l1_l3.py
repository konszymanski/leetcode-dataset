class Solution(object):

    def minCameraCover(self, root):
        self.v1_754 = 0
        v2_214 = {None}

        def v3_125(v4_859, v5_381=None):
            if v4_859:
                v3_125(v4_859.v6_350, v4_859)
                v3_125(v4_859.v7_328, v4_859)
                if v5_381 is None and v4_859 not in v2_214 or v4_859.v6_350 not in v2_214 or v4_859.v7_328 not in v2_214:
                    self.v1_754 += 1
                    v2_214.v8_242({v4_859, v5_381, v4_859.v6_350, v4_859.v7_328})
        v3_125(root)
        return self.v1_754