class Solution:
    def find132pattern(self, nums: List[int])  ->  bool:
        for v1_754 in range(len(nums) - 2):
            for v2_214 in range(v1_754 + 1, len(nums) - 1):
                for v3_125 in range(v2_214  +  1, len(nums)):
                    if nums[v1_754]  <  nums[v3_125]  <  nums[v2_214]:
                        return True
        return False
