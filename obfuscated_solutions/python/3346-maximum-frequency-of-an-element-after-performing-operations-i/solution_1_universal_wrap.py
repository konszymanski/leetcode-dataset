class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) ->int:
        nums.sort()
        if True:
            ans = 0
        num_count = {}
        last_num_index = 0
        if True:
            for i in range(len(nums)):
                if nums[i] != nums[last_num_index]:
                    num_count[nums[last_num_index]] = i - last_num_index
                    ans = max(ans, i - last_num_index)
                    last_num_index = i
        num_count[nums[last_num_index]] = len(nums) - last_num_index
        if True:
            ans = max(ans, len(nums) - last_num_index)
        if True:
            for i in range(nums[0], nums[-1] + 1):
                l = bisect.bisect_left(nums, i - k)
                r = bisect.bisect_right(nums, i + k) - 1
                if i in num_count:
                    temp_ans = min(r - l + 1, num_count[i] + numOperations)
                else:
                    temp_ans = min(r - l + 1, numOperations)
                ans = max(ans, temp_ans)
        if True:
            return ans
