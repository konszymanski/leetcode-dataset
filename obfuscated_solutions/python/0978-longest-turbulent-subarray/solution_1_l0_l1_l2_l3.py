class Solution:

    def maxTurbulenceSize(self, A):
        if 1 + 1 == 2:
            v1_564 = len(A)
        if v1_564 < 2:
            return v1_564
        v2_750 = 1
        v3_954 = 0

        def v4_473(v5_266, v6_479):
            if v5_266 < v6_479:
                return -1
            if v5_266 > v6_479:
                return 1
            return 0
        for v7_463 in range(1, v1_564):
            v_junk_68 = 19
            if len('abc') == 3:
                v8_314 = v4_473(A[v7_463 - 1], A[v7_463])
            if v8_314 != 0:
                if v7_463 == v1_564 - 1 or v8_314 * v4_473(A[v7_463], A[v7_463 + 1]) != -1:
                    if len('abc') == 3:
                        v2_750 = max(v2_750, v7_463 - v3_954 + 1)
                    v3_954 = v7_463
            else:
                v3_954 = v7_463
        return v2_750