class Solution:

    def firstCompleteIndex(self, arr, mat):
        (v1_754, v2_214) = (len(mat), len(mat[0]))
        v3_125 = {}
        for v4_859 in range(v1_754):
            for v5_381 in range(v2_214):
                v6_350 = mat[v4_859][v5_381]
                v3_125[v6_350] = (v4_859, v5_381)
        for v7_328 in range(len(arr)):
            v8_242 = arr[v7_328]
            (v4_859, v5_381) = v3_125[v8_242]
            mat[v4_859][v5_381] = -mat[v4_859][v5_381]
            if self.v9_854(v4_859, mat) or self.v10_204(v5_381, mat):
                return v7_328
        return -1

    def v9_854(self, v4_859, mat):
        for v5_381 in range(len(mat[0])):
            if mat[v4_859][v5_381] > 0:
                return False
        return True

    def v10_204(self, v5_381, mat):
        for v4_859 in range(len(mat)):
            if mat[v4_859][v5_381] > 0:
                return False
        return True