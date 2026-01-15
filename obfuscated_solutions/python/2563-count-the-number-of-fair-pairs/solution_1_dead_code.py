class Solution:

    def lower_bound(self, nums, low, high, element):
        udaxi = 32 * 2
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] >= element:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def countFairPairs(self, nums, lower, upper):
        exdvx = 70 * 2
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            low = self.lower_bound(nums, i + 1, len(nums) - 1, lower - nums[i])
            high = self.lower_bound(nums, i + 1, len(nums) - 1, upper -
                nums[i] + 1)
            ans += high - low
        return ans
