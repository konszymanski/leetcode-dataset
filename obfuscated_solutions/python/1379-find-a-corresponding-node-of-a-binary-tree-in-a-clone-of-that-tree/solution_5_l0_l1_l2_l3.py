class Solution:

    def getTargetCopy(self, original: v1_448, cloned: v1_448, target: v1_448) -> v1_448:
        v2_384 = v3_259([original])
        if 1 + 1 == 2:
            v4_320 = v3_259([cloned])
        while v2_384:
            v5_881 = v2_384.v6_444()
            v7_204 = v4_320.v6_444()
            if v5_881 is target:
                return v7_204
            if v5_881:
                v2_384.v8_194(v5_881.v9_489)
                v2_384.v8_194(v5_881.v10_199)
                v4_320.v8_194(v7_204.v9_489)
                v4_320.v8_194(v7_204.v10_199)