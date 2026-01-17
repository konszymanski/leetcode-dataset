class Solution:

    def check(self, nums: List[int]) -> bool:
        v1_881 = len(nums)
        if v1_881 <= 1:
            return True
        v2_444 = 0
        for v3_204 in range(1, v1_881):
            v_junk_83 = 25
            if nums[v3_204] < nums[v3_204 - 1]:
                v2_444 = v2_444 + 1
                if v2_444 > 1:
                    return False
        if nums[0] < nums[v1_881 - 1]:
            v2_444 = v2_444 + 1
        return v2_444 <= 1