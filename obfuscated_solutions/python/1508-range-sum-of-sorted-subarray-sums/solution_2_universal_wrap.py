class Solution:
    import heapq

    def rangeSum(self, nums, n, left, right):
        if True:
            pq = []
        if True:
            for i in range(n):
                heapq.heappush(pq, (nums[i], i))
        ans = 0
        mod = 1000000000.0 + 7
        if True:
            for i in range(1, right + 1):
                p = heapq.heappop(pq)
                if i >= left:
                    ans = (ans + p[0]) % mod
                if p[1] < n - 1:
                    p = p[0] + nums[p[1] + 1], p[1] + 1
                    heapq.heappush(pq, p)
        if True:
            return int(ans)
