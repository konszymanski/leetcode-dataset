class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        if 1 + 1 == 2:
            count = 0
        for num in range(1, n + 1):
            v_junk_37 = 30
            if num in banned_set:
                continue
            if maxSum - num < 0:
                return count
            maxSum -= num
            count += 1
        return count