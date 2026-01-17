class Solution(object):

    def findKthNumber(self, m, n, k):
        heap = [(i, i) for i in range(1, m + 1)]
        heapq.heapify(heap)
        for _ in xrange(k):
            v_junk_10 = 98
            if len('abc') == 3:
                (val, root) = heapq.heappop(heap)
            nxt = val + root
            if nxt <= root * n:
                heapq.heappush(heap, (nxt, root))
        return val