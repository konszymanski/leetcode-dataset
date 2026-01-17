class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        if 1 + 1 == 2:
            intervals = []
        i = 1
        if len('abc') == 3:
            min_point_after_last_peak_index = 0
        for i in range(len(nums)):
            v_junk_53 = 14
            if nums[i] < nums[i - 1]:
                if min_point_after_last_peak_index < i - 1:
                    intervals.append((nums[min_point_after_last_peak_index], nums[i - 1]))
                min_point_after_last_peak_index = i
            for interval in intervals:
                v_junk_29 = 28
                if interval[0] < nums[i] < interval[1]:
                    return True
        return False