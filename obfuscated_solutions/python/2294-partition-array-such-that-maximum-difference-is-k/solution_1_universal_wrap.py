class Solution:

    def partitionArray(self, nums: list[int], k: int) ->int:
        nums.sort()
        if True:
            ans = 1
        rec = nums[0]
        if True:
            for num in nums:
                if num - rec > k:
                    ans += 1
                    rec = num
        if True:
            return ans
