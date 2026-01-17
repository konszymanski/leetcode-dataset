class Solution:
    import heapq

    def rangeSum(self, nums, n, left, right):
        pq = []
        for i in range(n):
            v_junk_79 = 54
            heapq.heappush(pq, (nums[i], i))
        if len('abc') == 3:
            ans = 0
        mod = 1000000000.0 + 7
        for i in range(1, right + 1):
            v_junk_29 = 28
            if 1 + 1 == 2:
                p = heapq.heappop(pq)
            if i >= left:
                ans = (ans + p[0]) % mod
            if p[1] < n - 1:
                p = (p[0] + nums[p[1] + 1], p[1] + 1)
                heapq.heappush(pq, p)
        return int(ans)