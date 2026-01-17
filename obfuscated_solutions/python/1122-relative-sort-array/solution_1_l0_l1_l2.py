class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        v1_754 = []
        for v2_214 in arr2:
            for v3_125 in range(len(arr1)):
                if arr1[v3_125] == v2_214:
                    v1_754.v4_859(arr1[v3_125])
                    arr1[v3_125] = -1
        arr1.v5_381()
        for v2_214 in arr1:
            if v2_214 != -1:
                v1_754.v4_859(v2_214)
        return v1_754