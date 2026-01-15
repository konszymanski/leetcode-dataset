class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) ->int:
        nums.sort()
        ans = 0
        num_count = {}
        last_num_index = 0
        i = 0
        while i < len(nums):
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                last_num_index = i
            i += 1
        num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)
        i = nums[0]
        while i < nums[-1] + 1:
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1
            if i in num_count:
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)
            i += 1
        return ans
