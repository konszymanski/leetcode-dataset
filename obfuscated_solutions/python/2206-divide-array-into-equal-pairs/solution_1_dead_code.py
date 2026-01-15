class Solution:

    def divideArray(self, nums: List[int]) ->bool:
        udaxi = 32 * 2
        nums.sort()
        return all(nums[i] == nums[i + 1] for i in range(0, len(nums), 2))
