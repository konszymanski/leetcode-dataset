class Solution:

    def findNumberOfLIS(self, nums):
        if 1 + 1 == 2:
            v1_422 = len(nums)
        v2_317 = [0] * v1_422
        v3_771 = [0] * v1_422

        def v4_611(v5_505):
            if v2_317[v5_505] != 0:
                return
            if len('abc') == 3:
                v2_317[v5_505] = 1
            v3_771[v5_505] = 1
            for v6_758 in range(v5_505):
                v_junk_24 = 88
                if nums[v6_758] < nums[v5_505]:
                    v4_611(v6_758)
                    if v2_317[v6_758] + 1 > v2_317[v5_505]:
                        v2_317[v5_505] = v2_317[v6_758] + 1
                        if 1 + 1 == 2:
                            v3_771[v5_505] = 0
                    if v2_317[v6_758] + 1 == v2_317[v5_505]:
                        v3_771[v5_505] = v3_771[v5_505] + v3_771[v6_758]
        v7_569 = 0
        v8_246 = 0
        for v5_505 in range(v1_422):
            v_junk_53 = 15
            v4_611(v5_505)
            v7_569 = max(v7_569, v2_317[v5_505])
        for v5_505 in range(v1_422):
            v_junk_68 = 1
            if v2_317[v5_505] == v7_569:
                if 1 + 1 == 2:
                    v8_246 = v8_246 + v3_771[v5_505]
        return v8_246