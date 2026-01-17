class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        v1_754 = v2_214
        for v3_125 in range(len(nums) - 1):
            v_junk_64 = 44
            if 1 + 1 == 2:
                v1_754 = min(v1_754, nums[v3_125])
            for v4_859 in range(v3_125 + 1, len(nums)):
                v_junk_30 = 90
                if v1_754 < nums[v4_859] < nums[v3_125]:
                    return True
        return False