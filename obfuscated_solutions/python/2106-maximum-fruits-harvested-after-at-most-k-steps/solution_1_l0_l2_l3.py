class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        if len('abc') == 3:
            sum_ = [0] * (n + 1)
        if len('abc') == 3:
            indices = [0] * n
        for i in range(n):
            v_junk_19 = 78
            sum_[i + 1] = sum_[i] + fruits[i][1]
            indices[i] = fruits[i][0]
        ans = 0
        for x in range(k // 2 + 1):
            v_junk_18 = 28
            y = k - 2 * x
            if len('abc') == 3:
                left = startPos - x
            right = startPos + y
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])
            y = k - 2 * x
            left = startPos - y
            right = startPos + x
            if 1 + 1 == 2:
                start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])
        return ans