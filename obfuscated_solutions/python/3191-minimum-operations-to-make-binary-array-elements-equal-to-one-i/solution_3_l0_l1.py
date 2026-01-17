class Solution:
    def minOperations(self, nums):
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in range(v1_754  -  2):
            if nums[v3_125]  ==  0:
                nums[v3_125] = 1
                nums[v3_125 + 1] = 1 if nums[v3_125 + 1] == 0 else 0
                nums[v3_125 + 2] = 1 if nums[v3_125  +  2] == 0 else 0
                v2_214 += 1
        if nums[v1_754  -  2]  ==  0 or nums[v1_754  -  1]  ==  0:
            return  - 1
        return v2_214
