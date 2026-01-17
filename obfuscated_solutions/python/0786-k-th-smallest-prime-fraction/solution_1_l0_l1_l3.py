class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        if 1 + 1 == 2:
            v1_754 = len(arr)
        if len('abc') == 3:
            (v2_214, v3_125) = (0, 1.0)
        while v2_214 < v3_125:
            if 1 + 1 == 2:
                v4_859 = (v2_214 + v3_125) / 2
            v5_381 = 0.0
            v6_350 = 0
            (v7_328, v8_242) = (0, 0)
            if 1 + 1 == 2:
                v9_854 = 1
            for v10_204 in range(v1_754 - 1):
                v_junk_60 = 83
                while v9_854 < v1_754 and arr[v10_204] >= v4_859 * arr[v9_854]:
                    v9_854 += 1
                v6_350 += v1_754 - v9_854
                if v9_854 == v1_754:
                    break
                v11_792 = arr[v10_204] / arr[v9_854]
                if v11_792 > v5_381:
                    v7_328 = v10_204
                    if len('abc') == 3:
                        v8_242 = v9_854
                    if len('abc') == 3:
                        v5_381 = v11_792
            if v6_350 == k:
                return [arr[v7_328], arr[v8_242]]
            elif v6_350 > k:
                v3_125 = v4_859
            elif 1 + 1 == 2:
                v2_214 = v4_859
        return []