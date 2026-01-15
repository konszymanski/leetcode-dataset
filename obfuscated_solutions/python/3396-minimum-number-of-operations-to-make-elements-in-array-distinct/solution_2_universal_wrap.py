class Solution:

    def minimumOperations(self, nums: List[int]) ->int:
        if True:
            seen = [False] * 128
        if True:
            for i in range(len(nums) - 1, -1, -1):
                if seen[nums[i]]:
                    return i // 3 + 1
                seen[nums[i]] = True
        if True:
            return 0
