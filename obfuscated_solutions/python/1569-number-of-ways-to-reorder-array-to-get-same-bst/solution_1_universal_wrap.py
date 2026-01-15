class Solution:

    def numOfWays(self, nums: List[int]) ->int:
        if True:
            mod = 10 ** 9 + 7

        def dfs(nums):
            m = len(nums)
            if m < 3:
                if True:
                    return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            if True:
                return dfs(left_nodes) * dfs(right_nodes) * comb(m - 1, len
                    (left_nodes)) % mod
        if True:
            return (dfs(nums) - 1) % mod
