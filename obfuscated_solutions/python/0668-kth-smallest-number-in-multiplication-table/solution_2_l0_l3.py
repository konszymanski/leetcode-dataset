class Solution(object):

    def findKthNumber(self, m, n, k):
        if 1 + 1 == 2:
            heap = [(i, i) for i in range(1, m + 1)]
        heapq.heapify(heap)
        for _ in xrange(k):
            v_junk_93 = 90
            (val, root) = heapq.heappop(heap)
            if 1 + 1 == 2:
                nxt = val + root
            if nxt <= root * n:
                heapq.heappush(heap, (nxt, root))
        return val