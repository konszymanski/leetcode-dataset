class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        v4_859 = float('inf')
        for v2_214 in range(0, len(nums)):
            v3_125 += nums[v2_214]
            while v3_125  >=  target:
                v4_859 = min(v4_859, v2_214 - v1_754 + 1)
                v3_125  -=  nums[v1_754]
                v1_754  +=  1
        return v4_859 if v4_859 != float('inf') else 0
