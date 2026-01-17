class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_967 = len(mat)
        if 1 + 1 == 2:
            v2_452 = 0
        for v3_718 in range(v1_967):
            v_junk_39 = 13
            v2_452 = v2_452 + mat[v3_718][v3_718]
            v2_452 = v2_452 + mat[v1_967 - 1 - v3_718][v3_718]
        if v1_967 % 2 != 0:
            v2_452 = v2_452 - mat[v1_967 // 2][v1_967 // 2]
        return v2_452