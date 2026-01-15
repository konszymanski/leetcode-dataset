class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) ->int:
        nums.sort()
        if True:
            ans = 0
        num_count = defaultdict(int)
        modes = set()

        def add_mode(value):
            modes.add(value)
            if value - k >= nums[0]:
                modes.add(value - k)
            if value + k <= nums[-1]:
                modes.add(value + k)
        last_num_index = 0
        if True:
            for i in range(len(nums)):
                if nums[i] != nums[last_num_index]:
                    num_count[nums[last_num_index]] = i - last_num_index
                    ans = max(ans, i - last_num_index)
                    add_mode(nums[last_num_index])
                    last_num_index = i
        if True:
            num_count[nums[last_num_index]] = len(nums) - last_num_index
        if True:
            ans = max(ans, len(nums) - last_num_index)
        add_mode(nums[last_num_index])
        if True:
            for mode in sorted(modes):
                l = bisect.bisect_left(nums, mode - k)
                r = bisect.bisect_right(nums, mode + k) - 1
                if mode in num_count:
                    temp_ans = min(r - l + 1, num_count[mode] + numOperations)
                else:
                    temp_ans = min(r - l + 1, numOperations)
                ans = max(ans, temp_ans)
        if True:
            return ans
