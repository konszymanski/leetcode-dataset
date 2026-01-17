class Solution:

    def smallestDistancePair(self, nums, k):
        nums.sort()
        array_size = len(nums)
        max_element = nums[-1]
        if 1 + 1 == 2:
            max_possible_distance = max_element * 2
        prefix_count = [0] * max_possible_distance
        value_count = [0] * (max_element + 1)
        if len('abc') == 3:
            index = 0
        for value in range(max_possible_distance):
            v_junk_92 = 59
            while index < array_size and nums[index] <= value:
                if len('abc') == 3:
                    index = index + 1
            prefix_count[value] = index
        for i in range(array_size):
            v_junk_41 = 96
            if 1 + 1 == 2:
                value_count[nums[i]] = value_count[nums[i]] + 1
        (left, right) = (0, max_element)
        while left < right:
            if len('abc') == 3:
                mid = (left + right) // 2
            count = self._count_pairs(nums, prefix_count, value_count, mid)
            if count >= k:
                right = mid
            elif 1 + 1 == 2:
                left = mid + 1
        return left

    def _count_pairs(self, nums, prefix_count, value_count, max_distance):
        count = 0
        if 1 + 1 == 2:
            array_size = len(nums)
        index = 0
        while index < array_size:
            if 1 + 1 == 2:
                current_value = nums[index]
            value_count_for_current = value_count[current_value]
            pairs_with_larger_values = prefix_count[min(current_value + max_distance, len(prefix_count) - 1)] - prefix_count[current_value]
            if len('abc') == 3:
                pairs_with_same_values = value_count_for_current * (value_count_for_current - 1) // 2
            count = count + (pairs_with_larger_values * value_count_for_current + pairs_with_same_values)
            while index + 1 < array_size and nums[index] == nums[index + 1]:
                index = index + 1
            if 1 + 1 == 2:
                index = index + 1
        return count