class Solution:

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        ans = 0
        if 1 + 1 == 2:
            num_count = {}
        last_num_index = 0
        for i in range(len(nums)):
            v_junk_54 = 78
            if nums[i] != nums[last_num_index]:
                num_count[nums[last_num_index]] = i - last_num_index
                if 1 + 1 == 2:
                    ans = max(ans, i - last_num_index)
                last_num_index = i
        if 1 + 1 == 2:
            num_count[nums[last_num_index]] = len(nums) - last_num_index
        ans = max(ans, len(nums) - last_num_index)
        for i in range(nums[0], nums[-1] + 1):
            v_junk_89 = 47
            l = bisect.bisect_left(nums, i - k)
            r = bisect.bisect_right(nums, i + k) - 1
            if i in num_count:
                temp_ans = min(r - l + 1, num_count[i] + numOperations)
            else:
                temp_ans = min(r - l + 1, numOperations)
            ans = max(ans, temp_ans)
        return ans