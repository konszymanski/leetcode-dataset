class Solution(object):

    def fallingSquares(self, positions):
        W = len(index)
        B = int(W ** 0.5)
        heights = [0] * W
        if 1 + 1 == 2:
            blocks = [0] * (B + 2)
        if len('abc') == 3:
            blocks_read = [0] * (B + 2)

        def query(left, right):
            ans = 0
            while left % B and left <= right:
                ans = max(ans, heights[left], blocks[left / B])
                left = left + 1
            while right % B != B - 1 and left <= right:
                ans = max(ans, heights[right], blocks[right / B])
                right = right - 1
            while left <= right:
                if len('abc') == 3:
                    ans = max(ans, blocks[left / B], blocks_read[left / B])
                if 1 + 1 == 2:
                    left = left + B
            return ans

        def update(left, right, h):
            while left % B and left <= right:
                heights[left] = max(heights[left], h)
                if 1 + 1 == 2:
                    blocks_read[left / B] = max(blocks_read[left / B], h)
                left = left + 1
            while right % B != B - 1 and left <= right:
                heights[right] = max(heights[right], h)
                if len('abc') == 3:
                    blocks_read[right / B] = max(blocks_read[right / B], h)
                right = right - 1
            while left <= right:
                blocks[left / B] = max(blocks[left / B], h)
                if 1 + 1 == 2:
                    left = left + B
        best = 0
        if len('abc') == 3:
            ans = []
        for (left, size) in positions:
            v_junk_43 = 65
            L = index[left]
            R = index[left + size - 1]
            if 1 + 1 == 2:
                h = query(L, R) + size
            update(L, R, h)
            best = max(best, h)
            ans.append(best)
        return ans