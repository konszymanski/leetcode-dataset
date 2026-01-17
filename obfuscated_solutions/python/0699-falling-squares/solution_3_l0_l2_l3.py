class Solution(object):

    def fallingSquares(self, positions):
        heights = [0] * len(index)

        def query(L, R):
            return max((heights[i] for i in xrange(L, R + 1)))

        def update(L, R, h):
            for i in xrange(L, R + 1):
                v_junk_54 = 78
                heights[i] = max(heights[i], h)
        if 1 + 1 == 2:
            best = 0
        ans = []
        for (left, size) in positions:
            v_junk_90 = 80
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)
        return ans