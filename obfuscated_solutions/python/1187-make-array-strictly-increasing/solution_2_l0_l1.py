class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int])  ->  int:
        v1_754 = {-1: 0}
        arr2.v2_214()
        v3_125 = len(arr2)
        for v4_859 in range(len(arr1)):
            v5_381 = v6_350.v7_328(lambda: float('inf'))
            for v8_242 in v1_754:
                if arr1[v4_859] > v8_242:
                    v5_381[arr1[v4_859]] = min(v5_381[arr1[v4_859]], v1_754[v8_242])
                v9_854 = v10_204.v11_792(arr2, v8_242)
                if v9_854 < v3_125:
                    v5_381[arr2[v9_854]] = min(v5_381[arr2[v9_854]], 1 + v1_754[v8_242])
            v1_754 = v5_381
        return min(v1_754.v12_858()) if v1_754 else  - 1
