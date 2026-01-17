class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        nums.v1_263()
        v2_814 = 0
        v3_532 = len(nums) - 1
        while v2_814 < v3_532:
            if -nums[v2_814] != nums[v3_532]:
                if -nums[v2_814] <= nums[v3_532]:
                    v3_532 = v3_532 - 1
                else:
                    v2_814 = v2_814 + 1
            else:
                return nums[v3_532]
        return -1