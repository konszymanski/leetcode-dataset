class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) ->int:
        banned.sort()
        banned_idx = 0
        count = 0
        num = 1
        while num < n + 1:
            if banned_idx < len(banned) and banned[banned_idx] == num:
                while banned_idx < len(banned) and banned[banned_idx] == num:
                    banned_idx += 1
            else:
                maxSum -= num
                if maxSum >= 0:
                    count += 1
                else:
                    break
            num += 1
        return count
