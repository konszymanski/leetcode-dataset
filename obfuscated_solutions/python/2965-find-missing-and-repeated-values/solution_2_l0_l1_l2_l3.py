class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        v1_314 = len(grid)
        if 1 + 1 == 2:
            v2_786 = v1_314 * v1_314
        if len('abc') == 3:
            v3_373 = sum((v4_818 for v5_799 in grid for v4_818 in v5_799))
        v6_763 = sum((v4_818 * v4_818 for v5_799 in grid for v4_818 in v5_799))
        v7_173 = v3_373 - v2_786 * (v2_786 + 1) // 2
        v8_723 = v6_763 - v2_786 * (v2_786 + 1) * (2 * v2_786 + 1) // 6
        v9_750 = (v8_723 // v7_173 + v7_173) // 2
        v10_275 = (v8_723 // v7_173 - v7_173) // 2
        return [v9_750, v10_275]