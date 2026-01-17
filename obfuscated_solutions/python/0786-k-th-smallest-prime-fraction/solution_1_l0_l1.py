class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        v1_754 = len(arr)
        v2_214, v3_125 = 0, 1.0
        while v2_214 < v3_125:
            v4_859 = (v2_214  +  v3_125)  /  2
            v5_381 = 0.0
            v6_350 = 0
            v7_328, v8_242 = 0, 0
            v9_854 = 1
            for v10_204 in range(v1_754  -  1):
                while v9_854  <  v1_754 and arr[v10_204]  >=  v4_859 * arr[v9_854]:
                    v9_854  +=  1
                v6_350  +=  (v1_754 - v9_854)
                if v9_854 == v1_754:
                    break
                v11_792 = arr[v10_204] / arr[v9_854]
                if v11_792  >  v5_381:
                    v7_328 = v10_204
                    v8_242 = v9_854
                    v5_381 = v11_792
            if v6_350 == k:
                return [arr[v7_328], arr[v8_242]]
            elif v6_350  >  k:
                v3_125 = v4_859
            else:
                v2_214 = v4_859
        return []
