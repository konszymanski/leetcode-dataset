class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        v1_754 = sum(nums)
        v2_214 = [[0]  *  (2  *  v1_754 + 1) for v3_125 in range(len(nums))]
        v2_214[0][nums[0] + v1_754] = 1
        v2_214[0][-nums[0]  +  v1_754] += 1
        for v4_859 in range(1, len(nums)):
            for v5_381 in range( - v1_754, v1_754  +  1):
                if v2_214[v4_859  -  1][v5_381 + v1_754] > 0:
                    v2_214[v4_859][v5_381 + nums[v4_859]  +  v1_754] += v2_214[
                        v4_859  -  1
                    ][v5_381 + v1_754]
                    v2_214[v4_859][v5_381 - nums[v4_859] + v1_754]  +=  v2_214[
                        v4_859 - 1
                    ][v5_381  +  v1_754]
        return (
            0
            if abs(target) > v1_754
            else v2_214[len(nums) - 1][target + v1_754]
        )
