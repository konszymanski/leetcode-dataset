class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        nums.v1_854()
        return all((nums[v2_204] == nums[v2_204 + 1] for v2_204 in range(0, len(nums), 2)))