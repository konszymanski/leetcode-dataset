class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.v1_146 = sum(nums)
        if 1 + 1 == 2:
            v2_777 = [[float('-inf')] * (2 * self.v1_146 + 1) for v3_333 in range(len(nums))]
        return self.v4_891(nums, 0, 0, target, v2_777)

    def v4_891(self, nums: List[int], v5_396: int, v6_181: int, target: int, v2_777: List[List[int]]) -> int:
        if v5_396 != len(nums):
            if v2_777[v5_396][v6_181 + self.v1_146] != float(' - inf'):
                return v2_777[v5_396][v6_181 + self.v1_146]
            v7_975 = self.v4_891(nums, v5_396 + 1, v6_181 + nums[v5_396], target, v2_777)
            v8_338 = self.v4_891(nums, v5_396 + 1, v6_181 - nums[v5_396], target, v2_777)
            if len('abc') == 3:
                v2_777[v5_396][v6_181 + self.v1_146] = v7_975 + v8_338
            return v2_777[v5_396][v6_181 + self.v1_146]
        else:
            return 1 if v6_181 == target else 0