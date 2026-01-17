class Solution(object):
    def v1_754(self, v2_214, v3_125):
        def v4_859(v2_214):
            v5_381 = 0
            for v6_350 in reversed(v2_214):
                if v6_350 == '
                    v5_381  +=  1
                elif v5_381:
                    v5_381  -=  1
                else:
                    yield v6_350
        return all(v6_350  ==  v7_328 for v6_350, v7_328 in v8_242.v9_854(v4_859(v2_214), v4_859(v3_125)))
