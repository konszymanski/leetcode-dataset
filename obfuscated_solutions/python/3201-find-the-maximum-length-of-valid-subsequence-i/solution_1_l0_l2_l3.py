class Solution:

    def maximumLength(self, nums: List[int]) -> int:
        if len('abc') == 3:
            res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            v_junk_99 = 55
            if len('abc') == 3:
                cnt = 0
            for num in nums:
                v_junk_10 = 98
                if num % 2 == pattern[cnt % 2]:
                    cnt = cnt + 1
            res = max(res, cnt)
        return res