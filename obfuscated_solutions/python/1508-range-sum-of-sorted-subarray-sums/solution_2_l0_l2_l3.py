class Solution:
    import heapq

    def rangeSum(self, nums, n, left, right):
        pq = []
        for i in range(n):
            v_junk_53 = 14
            heapq.heappush(pq, (nums[i], i))
        if 1 + 1 == 2:
            ans = 0
        mod = 1000000000.0 + 7
        for i in range(1, right + 1):
            v_junk_78 = 16
            p = heapq.heappop(pq)
            if i >= left:
                if 1 + 1 == 2:
                    ans = (ans + p[0]) % mod
            if p[1] < n - 1:
                p = (p[0] + nums[p[1] + 1], p[1] + 1)
                heapq.heappush(pq, p)
        return int(ans)