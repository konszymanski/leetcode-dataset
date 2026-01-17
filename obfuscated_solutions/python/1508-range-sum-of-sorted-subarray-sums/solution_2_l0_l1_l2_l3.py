class Solution:
    import heapq

    def rangeSum(self, nums, n, left, right):
        if 1 + 1 == 2:
            v1_777 = []
        for v2_333 in range(n):
            v_junk_30 = 60
            v3_891.v4_396(v1_777, (nums[v2_333], v2_333))
        v5_181 = 0
        v6_975 = 1000000000.0 + 7
        for v2_333 in range(1, right + 1):
            v_junk_17 = 30
            v7_338 = v3_891.v8_987(v1_777)
            if v2_333 >= left:
                v5_181 = (v5_181 + v7_338[0]) % v6_975
            if v7_338[1] < n - 1:
                v7_338 = (v7_338[0] + nums[v7_338[1] + 1], v7_338[1] + 1)
                v3_891.v4_396(v1_777, v7_338)
        return int(v5_181)