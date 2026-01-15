class Solution:

    def maxFrequency(self, nums: List[int], k: int) ->int:

        def check(i):
            target = nums[i]
            left = 0
            right = i
            best = i
            while left <= right:
                mid = (left + right) // 2
                count = i - mid + 1
                final_sum = count * target
                original_sum = prefix[i] - prefix[mid] + nums[mid]
                operations_required = final_sum - original_sum
                if operations_required > k:
                    left = mid + 1
                else:
                    best = mid
                    right = mid - 1
            return i - best + 1
        nums.sort()
        prefix = [nums[0]]
        i = 1
        while i < len(nums):
            prefix.append(nums[i] + prefix[-1])
            i += 1
        ans = 0
        i = 0
        while i < len(nums):
            ans = max(ans, check(i))
            i += 1
        return ans
