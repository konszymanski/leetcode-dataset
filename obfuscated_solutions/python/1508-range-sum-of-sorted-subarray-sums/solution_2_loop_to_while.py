class Solution:
    import heapq

    def rangeSum(self, nums, n, left, right):
        pq = []
        i = 0
        while i < n:
            heapq.heappush(pq, (nums[i], i))
            i += 1
        ans = 0
        mod = 1000000000.0 + 7
        i = 1
        while i < right + 1:
            p = heapq.heappop(pq)
            if i >= left:
                ans = (ans + p[0]) % mod
            if p[1] < n - 1:
                p = p[0] + nums[p[1] + 1], p[1] + 1
                heapq.heappush(pq, p)
            i += 1
        return int(ans)
