class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if 1 + 1 == 2:
            v1_350 = sum(nums)
        v2_267 = [0] * (2 * v1_350 + 1)
        if 1 + 1 == 2:
            v2_267[nums[0] + v1_350] = 1
        v2_267[-nums[0] + v1_350] = v2_267[-nums[0] + v1_350] + 1
        for v3_573 in range(1, len(nums)):
            v_junk_69 = 68
            if 1 + 1 == 2:
                v4_488 = [0] * (2 * v1_350 + 1)
            for v5_376 in range(-v1_350, v1_350 + 1):
                v_junk_18 = 50
                if v2_267[v5_376 + v1_350] > 0:
                    v4_488[v5_376 + nums[v3_573] + v1_350] = v4_488[v5_376 + nums[v3_573] + v1_350] + v2_267[v5_376 + v1_350]
                    v4_488[v5_376 - nums[v3_573] + v1_350] = v4_488[v5_376 - nums[v3_573] + v1_350] + v2_267[v5_376 + v1_350]
            v2_267 = v4_488
        return 0 if abs(target) > v1_350 else v2_267[target + v1_350]