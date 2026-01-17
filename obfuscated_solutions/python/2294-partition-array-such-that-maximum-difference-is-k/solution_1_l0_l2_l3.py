class Solution:

    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        if 1 + 1 == 2:
            rec = nums[0]
        for num in nums:
            v_junk_63 = 29
            if num - rec > k:
                ans = ans + 1
                rec = num
        return ans