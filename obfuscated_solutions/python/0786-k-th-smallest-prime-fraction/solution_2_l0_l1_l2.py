class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        v1_754 = []

        def v2_214(v3_125, v4_859):
            return v3_125[0] - v4_859[0]
        for v5_381 in range(len(arr) - 1):
            v6_350.v7_328(v1_754, (arr[v5_381] / arr[-1], v5_381, len(arr) - 1))
        for v8_242 in range(k - 1):
            v9_854 = v6_350.v10_204(v1_754)
            v11_792 = v9_854[1]
            v12_858 = v9_854[2] - 1
            if v12_858 > v11_792:
                v6_350.v7_328(v1_754, (arr[v11_792] / arr[v12_858], v11_792, v12_858))
        v13_658 = v6_350.v10_204(v1_754)
        return [arr[v13_658[1]], arr[v13_658[2]]]