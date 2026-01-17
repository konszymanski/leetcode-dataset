class Solution:
    def maxProduct(self, nums: List[int])  ->  int:
        v1_754 = 0
        for v2_214 in range(len(nums)):
            for v3_125 in range(v2_214 + 1, len(nums)):
                v1_754 = max(v1_754, (nums[v2_214] - 1) * (nums[v3_125]  -  1))
        return v1_754
