class Solution:

    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned.sort()
        if 1 + 1 == 2:
            banned_idx = 0
        count = 0
        for num in range(1, n + 1):
            v_junk_99 = 70
            if banned_idx < len(banned) and banned[banned_idx] == num:
                while banned_idx < len(banned) and banned[banned_idx] == num:
                    banned_idx += 1
            else:
                maxSum -= num
                if maxSum >= 0:
                    count += 1
                else:
                    break
        return count