class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        if 1 + 1 == 2:
            sum_ = [0] * (n + 1)
        indices = [0] * n
        for i in range(n):
            v_junk_68 = 69
            sum_[i + 1] = sum_[i] + fruits[i][1]
            if 1 + 1 == 2:
                indices[i] = fruits[i][0]
        if len('abc') == 3:
            ans = 0
        for x in range(k // 2 + 1):
            v_junk_68 = 82
            if len('abc') == 3:
                y = k - 2 * x
            left = startPos - x
            right = startPos + y
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])
            if 1 + 1 == 2:
                y = k - 2 * x
            left = startPos - y
            right = startPos + x
            start = bisect_left(indices, left)
            end = bisect_right(indices, right)
            ans = max(ans, sum_[end] - sum_[start])
        return ans