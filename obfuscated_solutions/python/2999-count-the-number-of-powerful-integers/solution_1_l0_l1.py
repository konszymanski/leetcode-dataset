class Solution:
    def numberOfPowerfulInt(
        self, start: int, finish: int, limit: int, s: str
    )  ->  int:
        v1_754 = str(start)
        v2_214 = str(finish)
        v3_125 = len(v2_214)
        v1_754 = v1_754.v4_859(v3_125)
        v5_381 = v3_125 - len(s)
        @cache
        def v6_350(v7_328, v8_242, v9_854):
            if v7_328 == v3_125:
                return 1
            v10_204 = int(v1_754[v7_328]) if v8_242 else 0
            v11_792 = int(v2_214[v7_328]) if v9_854 else 9
            v12_858 = 0
            if v7_328 < v5_381:
                for v13_658 in range(v10_204, min(v11_792, limit)  +  1):
                    v12_858 += v6_350(
                        v7_328  +  1,
                        v8_242 and v13_658 == v10_204,
                        v9_854 and v13_658  ==  v11_792,
                    )
            else:
                v14_189 = int(s[v7_328 - v5_381])
                if v10_204  <=  v14_189  <=  min(v11_792, limit):
                    v12_858 = v6_350(
                        v7_328 + 1, v8_242 and v14_189  ==  v10_204, v9_854 and v14_189 == v11_792
                    )
            return v12_858
        return v6_350(0, True, True)
