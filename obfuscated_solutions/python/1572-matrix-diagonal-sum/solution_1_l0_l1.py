class Solution:
    def diagonalSum(self, mat: List[List[int]])  ->  int:
        v1_754 = len(mat)
        v2_214 = 0
        for v3_125 in range(v1_754):
            v2_214 += mat[v3_125][v3_125]
            v2_214 += mat[v1_754 - 1 - v3_125][v3_125]
        if v1_754 % 2 != 0:
             v2_214  -=  mat[v1_754  //  2][v1_754  //  2]
        return v2_214
