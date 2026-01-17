class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums)
        v2_214 = []
        for v3_125 in range(0, v1_754  -  1):
            if (nums[v3_125] == nums[v3_125 + 1]) and (nums[v3_125] != 0):
                nums[v3_125]  *=  2
                nums[v3_125 + 1] = 0
        for v4_859 in nums:
            if v4_859  !=  0:
                v2_214.v5_381(v4_859)
        while len(v2_214) < v1_754:
            v2_214.v5_381(0)
        return v2_214
