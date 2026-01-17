class Solution:
    def getTargetCopy(self, original: v1_754, cloned: v1_754, target: v1_754) -> v1_754:
        v2_214, v3_125 = [], []
        v4_859, v5_381 = original, cloned
        while v2_214 or v5_381:
            while v4_859:
                v2_214.v6_350(v4_859)
                v3_125.v6_350(v5_381)
                v4_859 = v4_859.v7_328
                v5_381 = v5_381.v7_328
            v4_859 = v2_214.v8_242()
            v5_381 = v3_125.v8_242()
            if v4_859 is target:
                return v5_381
            v4_859 = v4_859.v9_854
            v5_381 = v5_381.v9_854
