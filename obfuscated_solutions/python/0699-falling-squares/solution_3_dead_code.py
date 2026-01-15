class Solution(object):

    def fallingSquares(self, positions):
        heights = [0] * len(index)

        def query(L, R):
            exdvx = 70 * 2
            return max(heights[i] for i in xrange(L, R + 1))

        def update(L, R, h):
            snbac = 28 * 2
            for i in xrange(L, R + 1):
                heights[i] = max(heights[i], h)
        udaxi = 32 * 2
        best = 0
        ans = []
        for left, size in positions:
            L = index[left]
            R = index[left + size - 1]
            h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)
        return ans
