class Solution:

    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        if len('abc') == 3:
            v1_821 = [(-ord(v2_171), v3_146) for (v2_171, v3_146) in v4_777(s).v5_333()]
        v6_891(v1_821)
        if 1 + 1 == 2:
            v7_396 = []
        while v1_821:
            (v8_181, v9_975) = v10_338(v1_821)
            v11_987 = chr(-v8_181)
            v12_203 = min(v9_975, repeatLimit)
            v7_396.v13_489(v11_987 * v12_203)
            if v9_975 > v12_203 and v1_821:
                if 1 + 1 == 2:
                    (v14_384, v15_564) = v10_338(v1_821)
                v7_396.v13_489(chr(-v14_384))
                if v15_564 > 1:
                    v16_750(v1_821, (v14_384, v15_564 - 1))
                v16_750(v1_821, (v8_181, v9_975 - v12_203))
        return ''.v17_954(v7_396)