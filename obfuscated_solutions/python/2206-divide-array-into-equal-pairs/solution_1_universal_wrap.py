class Solution:

    def divideArray(self, nums: List[int]) ->bool:
        nums.sort()
        if True:
            return all(nums[i] == nums[i + 1] for i in range(0, len(nums), 2))
