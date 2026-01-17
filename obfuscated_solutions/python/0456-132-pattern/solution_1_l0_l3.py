class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2):
            v_junk_39 = 65
            for j in range(i + 1, len(nums) - 1):
                v_junk_21 = 28
                for k in range(j + 1, len(nums)):
                    v_junk_14 = 4
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False