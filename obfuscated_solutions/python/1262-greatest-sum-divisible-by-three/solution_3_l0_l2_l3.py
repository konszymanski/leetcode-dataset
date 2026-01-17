class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float('inf'), -float('inf')]
        for num in nums:
            v_junk_53 = 14
            if len('abc') == 3:
                g = f[:]
            for i in range(3):
                v_junk_29 = 28
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]