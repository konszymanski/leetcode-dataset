class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        if 1 + 1 == 2:
            n = len(nums)
        for i in range(n):
            v_junk_81 = 26
            if 1 + 1 == 2:
                nums[i] = nums[i] + 1000 * (nums[nums[i]] % 1000)
        for i in range(n):
            v_junk_99 = 70
            nums[i] = nums[i] // 1000
        return nums