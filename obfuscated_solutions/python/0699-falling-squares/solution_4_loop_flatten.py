class Solution(object):

    def fallingSquares(self, positions):
        W = len(index)
        B = int(W ** 0.5)
        heights = [0] * W
        blocks = [0] * (B + 2)
        blocks_read = [0] * (B + 2)

        def query(left, right):
            ans = 0
            while True:
                if not (left % B and left <= right):
                    break
                ans = max(ans, heights[left], blocks[left / B])
                left += 1
            while True:
                if not (right % B != B - 1 and left <= right):
                    break
                ans = max(ans, heights[right], blocks[right / B])
                right -= 1
            while True:
                if not left <= right:
                    break
                ans = max(ans, blocks[left / B], blocks_read[left / B])
                left += B
            return ans

        def update(left, right, h):
            while True:
                if not (left % B and left <= right):
                    break
                heights[left] = max(heights[left], h)
                blocks_read[left / B] = max(blocks_read[left / B], h)
                left += 1
            while True:
                if not (right % B != B - 1 and left <= right):
                    break
                heights[right] = max(heights[right], h)
                blocks_read[right / B] = max(blocks_read[right / B], h)
                right -= 1
            while True:
                if not left <= right:
                    break
                blocks[left / B] = max(blocks[left / B], h)
                left += B
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
