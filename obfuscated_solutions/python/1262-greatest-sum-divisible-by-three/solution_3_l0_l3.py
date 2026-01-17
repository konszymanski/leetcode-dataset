class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            f = [0, -float('inf'), -float('inf')]
        for num in nums:
            v_junk_45 = 1
            g = f[:]
            for i in range(3):
                v_junk_63 = 29
                g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num)
            f = g
        return f[0]