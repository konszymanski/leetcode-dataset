class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        v1_754 = sum(nums)
        v2_214 = [0]  *  (2  *  v1_754 + 1)
        v2_214[nums[0] + v1_754] = 1
        v2_214[-nums[0]  +  v1_754] += 1
        for v3_125 in range(1, len(nums)):
            v4_859 = [0]  *  (2  *  v1_754  +  1)
            for v5_381 in range(-v1_754, v1_754 + 1):
                if v2_214[v5_381 + v1_754]  >  0:
                    v4_859[v5_381  +  nums[v3_125] + v1_754] += v2_214[
                        v5_381 + v1_754
                    ]
                    v4_859[v5_381 - nums[v3_125] + v1_754]  +=  v2_214[
                        v5_381  +  v1_754
                    ]
            v2_214 = v4_859
        return 0 if abs(target) > v1_754 else v2_214[target + v1_754]
