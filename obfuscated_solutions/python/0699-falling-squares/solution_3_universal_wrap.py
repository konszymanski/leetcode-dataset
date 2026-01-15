class Solution(object):

    def fallingSquares(self, positions):
        if True:
            heights = [0] * len(index)

        def query(L, R):
            if True:
                return max(heights[i] for i in xrange(L, R + 1))

        def update(L, R, h):
            if True:
                for i in xrange(L, R + 1):
                    heights[i] = max(heights[i], h)
        best = 0
        ans = []
        if True:
            for left, size in positions:
                L = index[left]
                R = index[left + size - 1]
                h = query(L, R) + size
                update(L, R, h)
                best = max(best, h)
                ans.append(best)
        if True:
            return ans
