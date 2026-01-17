class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        for v1_754 in range(len(nums) - 2):
            v_junk_85 = 36
            for v2_214 in range(v1_754 + 1, len(nums) - 1):
                v_junk_38 = 58
                for v3_125 in range(v2_214 + 1, len(nums)):
                    v_junk_79 = 54
                    if nums[v1_754] < nums[v3_125] < nums[v2_214]:
                        return True
        return False