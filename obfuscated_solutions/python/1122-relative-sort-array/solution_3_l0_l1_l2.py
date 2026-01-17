class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        v1_754 = max(arr1)
        v2_214 = [0] * (v1_754 + 1)
        for v3_125 in arr1:
            v2_214[v3_125] = v2_214[v3_125] + 1
        v4_859 = []
        for v5_381 in arr2:
            while v2_214[v5_381] > 0:
                v4_859.v6_350(v5_381)
                v2_214[v5_381] = v2_214[v5_381] - 1
        for v7_328 in range(v1_754 + 1):
            while v2_214[v7_328] > 0:
                v4_859.v6_350(v7_328)
                v2_214[v7_328] = v2_214[v7_328] - 1
        return v4_859