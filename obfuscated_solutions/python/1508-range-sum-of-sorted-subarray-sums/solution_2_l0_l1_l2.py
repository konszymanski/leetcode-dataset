class Solution:
    import heapq

    def rangeSum(self, nums, n, left, right):
        v1_754 = []
        for v2_214 in range(n):
            v3_125.v4_859(v1_754, (nums[v2_214], v2_214))
        v5_381 = 0
        v6_350 = 1000000000.0 + 7
        for v2_214 in range(1, right + 1):
            v7_328 = v3_125.v8_242(v1_754)
            if v2_214 >= left:
                v5_381 = (v5_381 + v7_328[0]) % v6_350
            if v7_328[1] < n - 1:
                v7_328 = (v7_328[0] + nums[v7_328[1] + 1], v7_328[1] + 1)
                v3_125.v4_859(v1_754, v7_328)
        return int(v5_381)