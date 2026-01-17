class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        for v1_928 in range(len(nums) - 2):
            v_junk_87 = 34
            for v2_990 in range(v1_928 + 1, len(nums) - 1):
                v_junk_55 = 45
                for v3_106 in range(v2_990 + 1, len(nums)):
                    v_junk_58 = 13
                    if nums[v1_928] < nums[v3_106] < nums[v2_990]:
                        return True
        return False