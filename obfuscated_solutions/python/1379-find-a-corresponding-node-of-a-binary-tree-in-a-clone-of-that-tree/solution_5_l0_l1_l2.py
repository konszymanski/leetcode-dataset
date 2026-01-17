class Solution:

    def getTargetCopy(self, original: v1_754, cloned: v1_754, target: v1_754) -> v1_754:
        v2_214 = v3_125([original])
        v4_859 = v3_125([cloned])
        while v2_214:
            v5_381 = v2_214.v6_350()
            v7_328 = v4_859.v6_350()
            if v5_381 is target:
                return v7_328
            if v5_381:
                v2_214.v8_242(v5_381.v9_854)
                v2_214.v8_242(v5_381.v10_204)
                v4_859.v8_242(v7_328.v9_854)
                v4_859.v8_242(v7_328.v10_204)