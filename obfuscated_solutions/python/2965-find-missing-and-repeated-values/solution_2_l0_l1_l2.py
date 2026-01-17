class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        v1_754 = len(grid)
        v2_214 = v1_754 * v1_754
        v3_125 = sum((v4_859 for v5_381 in grid for v4_859 in v5_381))
        v6_350 = sum((v4_859 * v4_859 for v5_381 in grid for v4_859 in v5_381))
        v7_328 = v3_125 - v2_214 * (v2_214 + 1) // 2
        v8_242 = v6_350 - v2_214 * (v2_214 + 1) * (2 * v2_214 + 1) // 6
        v9_854 = (v8_242 // v7_328 + v7_328) // 2
        v10_204 = (v8_242 // v7_328 - v7_328) // 2
        return [v9_854, v10_204]