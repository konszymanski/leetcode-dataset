class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int
        ) ->int:
        n = len(fruits)
        sum_ = [0] * (n + 1)
        indices = [0] * n
        i = 0
        while i < n:
            sum_[i + 1] = sum_[i] + fruits[i][1]
            indices[i] = fruits[i][0]
            i += 1
        ans = 0
        x = 0
        while x < k // 2 + 1:
            y = k - 2 * x
            left = startPos - x
            right = startPos + y
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])
            y = k - 2 * x
            left = startPos - y
            right = startPos + x
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])
            x += 1
        return ans
