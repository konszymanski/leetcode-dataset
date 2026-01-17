class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        v1_954 = sum(nums)
        if 1 + 1 == 2:
            v2_473 = [[0] * (2 * v1_954 + 1) for v3_266 in range(len(nums))]
        v2_473[0][nums[0] + v1_954] = 1
        v2_473[0][-nums[0] + v1_954] = v2_473[0][-nums[0] + v1_954] + 1
        for v4_479 in range(1, len(nums)):
            v_junk_56 = 29
            for v5_463 in range(-v1_954, v1_954 + 1):
                v_junk_84 = 52
                if v2_473[v4_479 - 1][v5_463 + v1_954] > 0:
                    v2_473[v4_479][v5_463 + nums[v4_479] + v1_954] = v2_473[v4_479][v5_463 + nums[v4_479] + v1_954] + v2_473[v4_479 - 1][v5_463 + v1_954]
                    v2_473[v4_479][v5_463 - nums[v4_479] + v1_954] = v2_473[v4_479][v5_463 - nums[v4_479] + v1_954] + v2_473[v4_479 - 1][v5_463 + v1_954]
        return 0 if abs(target) > v1_954 else v2_473[len(nums) - 1][target + v1_954]