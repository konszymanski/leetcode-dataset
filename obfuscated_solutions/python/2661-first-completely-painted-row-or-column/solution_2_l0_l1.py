class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        v1_754, v2_214 = len(mat), len(mat[0])
        v3_125, v4_859 = [0] * v1_754, [0] * v2_214
        v5_381 = {}
        for v6_350 in range(v1_754):
            for v7_328 in range(v2_214):
                v5_381[mat[v6_350][v7_328]] = [v6_350, v7_328]
        for v8_242 in range(len(arr)):
            v9_854 = arr[v8_242]
            v6_350, v7_328 = v5_381[v9_854]
            v3_125[v6_350]  +=  1
            v4_859[v7_328]  +=  1
            if v3_125[v6_350]  ==  v2_214 or v4_859[v7_328] == v1_754:
                return v8_242
        return  - 1
