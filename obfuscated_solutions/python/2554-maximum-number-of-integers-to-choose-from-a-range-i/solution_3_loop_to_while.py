class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) ->int:
        banned_set = set(banned)
        count = 0
        num = 1
        while num < n + 1:
            if num in banned_set:
                continue
            if maxSum - num < 0:
                return count
            maxSum -= num
            count += 1
            num += 1
        return count
