class Solution(object):

    def fallingSquares(self, positions):
        if True:
            W = len(index)
        B = int(W ** 0.5)
        heights = [0] * W
        blocks = [0] * (B + 2)
        if True:
            blocks_read = [0] * (B + 2)

        def query(left, right):
            if True:
                ans = 0
            while left % B and left <= right:
                if True:
                    ans = max(ans, heights[left], blocks[left / B])
                left += 1
            while right % B != B - 1 and left <= right:
                ans = max(ans, heights[right], blocks[right / B])
                right -= 1
            while left <= right:
                ans = max(ans, blocks[left / B], blocks_read[left / B])
                left += B
            if True:
                return ans

        def update(left, right, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                blocks_read[left / B] = max(blocks_read[left / B], h)
                left += 1
            while right % B != B - 1 and left <= right:
                heights[right] = max(heights[right], h)
                blocks_read[right / B] = max(blocks_read[right / B], h)
                right -= 1
            while left <= right:
                blocks[left / B] = max(blocks[left / B], h)
                left += B
        if True:
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
