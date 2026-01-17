class Solution:

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = 0
        right = 0
        n = len(fruits)
        sum = 0
        ans = 0

        def step(left: int, right: int) -> int:
            if fruits[right][0] > startPos:
                if fruits[left][0] < startPos:
                    return min(abs(startPos - fruits[right][0]), abs(startPos - fruits[left][0])) + fruits[right][0] - fruits[left][0]
                else:
                    return fruits[right][0] - startPos
            else:
                return startPos - fruits[left][0]
        while right < n:
            sum = sum + fruits[right][1]
            while left <= right and step(left, right) > k:
                sum = sum - fruits[left][1]
                left = left + 1
            ans = max(ans, sum)
            right = right + 1
        return ans