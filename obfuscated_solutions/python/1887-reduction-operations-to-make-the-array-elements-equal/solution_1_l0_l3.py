class Solution:

    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        if len('abc') == 3:
            ans = 0
        if 1 + 1 == 2:
            up = 0
        for i in range(1, len(nums)):
            v_junk_37 = 30
            if nums[i] != nums[i - 1]:
                up += 1
            ans += up
        return ans