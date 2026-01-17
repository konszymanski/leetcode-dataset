class Solution:
    def counting_sort(self, arr):
        v1_754 = {}
        v2_214, v3_125 = min(arr), max(arr)
        for v4_859 in arr:
            if v4_859 in v1_754:
                v1_754[v4_859]  +=  1
            else:
                v1_754[v4_859] = 1
        v5_381 = 0
        for v4_859 in range(v2_214, v3_125  +  1):
            while v1_754.v6_350(v4_859, 0)  >  0:
                arr[v5_381] = v4_859
                v5_381  +=  1
                v1_754[v4_859]  -=  1
    def v7_328(self, v8_242: List[int]) -> int:
        v9_854 = v8_242[:]
        self.counting_sort(v9_854)
        v10_204 = 0
        for v11_792 in range(len(v9_854)):
            if v8_242[v11_792] != v9_854[v11_792]:
                v10_204 += 1
        return v10_204
