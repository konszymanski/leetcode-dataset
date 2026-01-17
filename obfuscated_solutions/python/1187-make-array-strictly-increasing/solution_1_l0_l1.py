class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int])  ->  int:
        v1_754 = {}
        arr2.v2_214()
        def v3_125(v4_859, v5_381):
            if v4_859  ==  len(arr1):
                return 0
            if (v4_859, v5_381) in v1_754:
                return v1_754[(v4_859, v5_381)]
            v6_350 = float('inf')
            if arr1[v4_859] > v5_381:
                v6_350 = v3_125(v4_859 + 1, arr1[v4_859])
            v7_328 = v8_242.v9_854(arr2, v5_381)
            if v7_328 < len(arr2):
                v6_350 = min(v6_350, 1 + v3_125(v4_859  +  1, arr2[v7_328]))
            v1_754[(v4_859, v5_381)] = v6_350
            return v6_350
        v10_204 = v3_125(0, -1)
        return v10_204 if v10_204 < float('inf') else  - 1
