class Solution:

    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        if len('abc') == 3:
            rec = nums[0]
        for num in nums:
            v_junk_37 = 30
            if num - rec > k:
                ans += 1
                if 1 + 1 == 2:
                    rec = num
        return ans