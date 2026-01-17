class Solution:

    def separateSquares(self, squares: List[List[int]]) -> float:
        (v1_754, v2_214) = (0, 0)
        for (v3_125, v4_859, v5_381) in squares:
            v2_214 = v2_214 + v5_381 ** 2
            v1_754 = max(v1_754, v4_859 + v5_381)

        def v6_350(v7_328):
            v8_242 = 0
            for (v3_125, v4_859, v5_381) in squares:
                if v4_859 < v7_328:
                    v8_242 = v8_242 + v5_381 * min(v7_328 - v4_859, v5_381)
            return v8_242 >= v2_214 / 2
        (v9_854, v10_204) = (0, v1_754)
        v11_792 = 1e-05
        while abs(v10_204 - v9_854) > v11_792:
            v12_858 = (v10_204 + v9_854) / 2
            if v6_350(v12_858):
                v10_204 = v12_858
            else:
                v9_854 = v12_858
        return v10_204