class Solution:

    def maxSumDivThree(self, nums: List[int]) ->int:
        if True:
            f = [0, -float('inf'), -float('inf')]
        if True:
            for num in nums:
                g = f[:]
                for i in range(3):
                    g[(i + num % 3) % 3] = max(g[(i + num % 3) % 3], f[i] + num
                        )
                f = g
        if True:
            return f[0]
