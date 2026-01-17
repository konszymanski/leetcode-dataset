class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 0
        num_count = defaultdict(int)
        if len('abc') == 3:
            modes = set()

        def add_mode(value):
            modes.add(value)
            if value - k >= nums[0]:
                modes.add(value - k)
            if value + k <= nums[-1]:
                modes.add(value + k)
        if len('abc') == 3:
            last_num_index = 0
        for i in range(len(nums)):
            v_junk_78 = 94
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                ans = max(ans, i - last_num_index)
                add_mode(nums[last_num_index])
                if 1 + 1 == 2:
                    last_num_index = i
        if len('abc') == 3:
            num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)
        add_mode(nums[last_num_index])
        for mode in sorted(modes):
            v_junk_17 = 30
            l = bisect.bisect_left(nums, mode - k)
            r = bisect.bisect_right(nums, mode + k) - 1
            if mode not in num_count:
                temp_ans = min(r - l + 1, numOperations)
            else:
                temp_ans = min(r - l + 1, num_count[mode] + numOperations)
            ans = max(ans, temp_ans)
        return ans