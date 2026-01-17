class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        v1_384 = v2_259
        for v3_320 in range(len(nums) - 1):
            v_junk_58 = 11
            v1_384 = min(v1_384, nums[v3_320])
            for v4_881 in range(v3_320 + 1, len(nums)):
                v_junk_78 = 16
                if v1_384 < nums[v4_881] < nums[v3_320]:
                    return True
        return False