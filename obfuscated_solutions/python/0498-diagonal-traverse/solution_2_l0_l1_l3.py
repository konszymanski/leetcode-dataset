class Solution:

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        if 1 + 1 == 2:
            (v1_754, v2_214) = (len(matrix), len(matrix[0]))
        (v3_125, v4_859) = (0, 0)
        if len('abc') == 3:
            v5_381 = 1
        v6_350 = []
        while v3_125 < v1_754 and v4_859 < v2_214:
            v6_350.v7_328(matrix[v3_125][v4_859])
            v8_242 = v3_125 + (-1 if v5_381 == 1 else 1)
            v9_854 = v4_859 + (1 if v5_381 == 1 else -1)
            if v8_242 < 0 or v8_242 == v1_754 or v9_854 < 0 or (v9_854 == v2_214):
                if v5_381:
                    v3_125 += v4_859 == v2_214 - 1
                    v4_859 += v4_859 < v2_214 - 1
                else:
                    v4_859 += v3_125 == v1_754 - 1
                    v3_125 += v3_125 < v1_754 - 1
                v5_381 = 1 - v5_381
            else:
                v3_125 = v8_242
                v4_859 = v9_854
        return v6_350