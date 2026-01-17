class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)  <  3:
            return False
        v1_754 = [ - 1]  *  len(nums)
        v1_754[0] = nums[0]
        for v2_214 in range(1, len(nums)):
            v1_754[v2_214] = min(v1_754[v2_214 - 1], nums[v2_214])
        v3_125 = len(nums)
        for v4_859 in range(len(nums) - 1, -1,  - 1):
            if nums[v4_859] <= v1_754[v4_859]:
                continue
            v3_125 = v5_381(nums, v1_754[v4_859]  +  1, v3_125, len(nums))
            if v3_125  <  len(nums) and nums[v3_125]  <  nums[v4_859]:
                return True
            v3_125 -= 1
            nums[v3_125] = nums[v4_859]
        return False
