class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.v1_754()
        return all(nums[v2_214] == nums[v2_214 + 1] for v2_214 in range(0, len(nums), 2))
