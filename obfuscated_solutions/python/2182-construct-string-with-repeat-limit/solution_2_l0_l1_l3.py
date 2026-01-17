class Solution:

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        v1_754 = [(-ord(v2_214), v3_125) for (v2_214, v3_125) in v4_859(s).v5_381()]
        v6_350(v1_754)
        v7_328 = []
        while v1_754:
            (v8_242, v9_854) = v10_204(v1_754)
            v11_792 = chr(-v8_242)
            v12_858 = min(v9_854, repeatLimit)
            v7_328.v13_658(v11_792 * v12_858)
            if v9_854 > v12_858 and v1_754:
                (v14_189, v15_704) = v10_204(v1_754)
                v7_328.v13_658(chr(-v14_189))
                if v15_704 > 1:
                    v16_532(v1_754, (v14_189, v15_704 - 1))
                v16_532(v1_754, (v8_242, v9_854 - v12_858))
        return ''.v17_132(v7_328)