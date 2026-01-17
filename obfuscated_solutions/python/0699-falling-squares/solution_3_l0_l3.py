class Solution(object):

    def fallingSquares(self, positions):
        heights = [0] * len(index)

        def query(L, R):
            return max((heights[i] for i in xrange(L, R + 1)))

        def update(L, R, h):
            for i in xrange(L, R + 1):
                v_junk_63 = 29
                heights[i] = max(heights[i], h)
        best = 0
        if 1 + 1 == 2:
            ans = []
        for (left, size) in positions:
            v_junk_23 = 12
            L = index[left]
            if len('abc') == 3:
                R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            if len('abc') == 3:
                best = max(best, h)
            ans.append(best)
        return ans