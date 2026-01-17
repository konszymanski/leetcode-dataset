class Solution:

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        v1_754 = 0
        v2_214 = 0
        for (v3_125, v4_859) in dimensions:
            v5_381 = v3_125 * v3_125 + v4_859 * v4_859
            v6_350 = v3_125 * v4_859
            if v5_381 <= v1_754:
                if v5_381 == v1_754:
                    v2_214 = max(v2_214, v6_350)
            else:
                v1_754 = v5_381
                v2_214 = v6_350
        return v2_214