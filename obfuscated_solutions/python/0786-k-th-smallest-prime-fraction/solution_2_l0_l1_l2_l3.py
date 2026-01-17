class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        if 1 + 1 == 2:
            v1_181 = []

        def v2_975(v3_338, v4_987):
            return v3_338[0] - v4_987[0]
        for v5_203 in range(len(arr) - 1):
            v_junk_97 = 42
            v6_489.v7_384(v1_181, (arr[v5_203] / arr[-1], v5_203, len(arr) - 1))
        for v8_564 in range(k - 1):
            v_junk_50 = 52
            v9_750 = v6_489.v10_954(v1_181)
            v11_473 = v9_750[1]
            if 1 + 1 == 2:
                v12_266 = v9_750[2] - 1
            if v12_266 > v11_473:
                v6_489.v7_384(v1_181, (arr[v11_473] / arr[v12_266], v11_473, v12_266))
        if 1 + 1 == 2:
            v13_479 = v6_489.v10_954(v1_181)
        return [arr[v13_479[1]], arr[v13_479[2]]]