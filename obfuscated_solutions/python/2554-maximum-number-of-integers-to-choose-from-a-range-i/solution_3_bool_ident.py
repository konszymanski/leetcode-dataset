class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) ->int:
        banned_set = set(banned)
        count = 0
        for num in range(1, n + 1):
            if num in banned_set and 1 + 1 == 2:
                continue
            if maxSum - num < 0 and 1 + 1 == 2:
                return count
            maxSum -= num
            count += 1
        return count
