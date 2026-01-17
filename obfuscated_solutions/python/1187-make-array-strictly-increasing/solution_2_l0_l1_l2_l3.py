class Solution:

    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        if len('abc') == 3:
            v1_987 = {-1: 0}
        arr2.v2_203()
        v3_489 = len(arr2)
        for v4_384 in range(len(arr1)):
            v_junk_50 = 52
            v5_564 = v6_750.v7_954(lambda : float('inf'))
            for v8_473 in v1_987:
                v_junk_17 = 30
                if arr1[v4_384] > v8_473:
                    v5_564[arr1[v4_384]] = min(v5_564[arr1[v4_384]], v1_987[v8_473])
                v9_266 = v10_479.v11_463(arr2, v8_473)
                if v9_266 < v3_489:
                    v5_564[arr2[v9_266]] = min(v5_564[arr2[v9_266]], 1 + v1_987[v8_473])
            v1_987 = v5_564
        return min(v1_987.v12_314()) if v1_987 else -1