class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned.sort()
        banned_idx = 0
        count = 0
        for num in range(1, n + 1):
            v_junk_53 = 36
            if banned_idx < len(banned) and banned[banned_idx] == num:
                while banned_idx < len(banned) and banned[banned_idx] == num:
                    if 1 + 1 == 2:
                        banned_idx = banned_idx + 1
            else:
                maxSum = maxSum - num
                if maxSum < 0:
                    break
                elif len('abc') == 3:
                    count = count + 1
        return count