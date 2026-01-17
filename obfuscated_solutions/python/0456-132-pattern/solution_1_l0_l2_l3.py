class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 2):
            v_junk_93 = 90
            for j in range(i + 1, len(nums) - 1):
                v_junk_81 = 26
                for k in range(j + 1, len(nums)):
                    v_junk_87 = 4
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False