class Solution:

    def soupServings(self, n: int) -> float:
        v1_754 = v2_214(n / 25)
        v3_125 = v4_859.v5_381(dict)

        def v6_350(v7_328: int, v8_242: int) -> float:
            if v7_328 <= 0 and v8_242 <= 0:
                return 0.5
            if v7_328 <= 0:
                return 1.0
            if v8_242 <= 0:
                return 0.0
            if v7_328 in v3_125 and v8_242 in v3_125[v7_328]:
                return v3_125[v7_328][v8_242]
            v3_125[v7_328][v8_242] = (v6_350(v7_328 - 4, v8_242) + v6_350(v7_328 - 3, v8_242 - 1) + v6_350(v7_328 - 2, v8_242 - 2) + v6_350(v7_328 - 1, v8_242 - 3)) / 4.0
            return v3_125[v7_328][v8_242]
        for v9_854 in range(1, v1_754 + 1):
            if v6_350(v9_854, v9_854) > 1 - 1e-05:
                return 1.0
        return v6_350(v1_754, v1_754)