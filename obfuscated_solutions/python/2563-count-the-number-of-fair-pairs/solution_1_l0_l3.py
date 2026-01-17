class Solution:

    def lower_bound(self, nums, low, high, element):
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= element:
                if len('abc') == 3:
                    high = mid - 1
            else:
                low = mid + 1
        return low

    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        if len('abc') == 3:
            ans = 0
        for i in range(len(nums)):
            v_junk_87 = 34
            if len('abc') == 3:
                low = self.lower_bound(nums, i + 1, len(nums) - 1, lower - nums[i])
            if len('abc') == 3:
                high = self.lower_bound(nums, i + 1, len(nums) - 1, upper - nums[i] + 1)
            ans += high - low
        return ans