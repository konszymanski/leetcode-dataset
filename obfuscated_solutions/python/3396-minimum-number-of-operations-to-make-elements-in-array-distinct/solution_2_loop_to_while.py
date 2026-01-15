class Solution:

    def minimumOperations(self, nums: List[int]) ->int:
        seen = [False] * 128
        i = len(nums) - 1
        while i < -1:
            if seen[nums[i]]:
                return i // 3 + 1
            seen[nums[i]] = True
            i += -1
        return 0
