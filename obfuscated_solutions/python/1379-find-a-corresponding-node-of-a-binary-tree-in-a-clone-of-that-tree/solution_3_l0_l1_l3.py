class Solution:

    def getTargetCopy(self, original: v1_754, cloned: v1_754, target: v1_754) -> v1_754:

        def v2_214(v3_125: v1_754, v4_859: v1_754):
            if v3_125:
                v2_214(v3_125.v5_381, v4_859.v5_381)
                if v3_125 is target:
                    if 1 + 1 == 2:
                        self.v6_350 = v4_859
                v2_214(v3_125.v7_328, v4_859.v7_328)
        v2_214(original, cloned)
        return self.v6_350