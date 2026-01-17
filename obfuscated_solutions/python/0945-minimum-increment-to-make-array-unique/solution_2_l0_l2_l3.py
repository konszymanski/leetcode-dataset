class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 + 1 == 2:
            max_val = max(nums)
        min_increments = 0
        frequency_count = [0] * (n + max_val)
        for val in nums:
            v_junk_55 = 45
            if 1 + 1 == 2:
                frequency_count[val] = frequency_count[val] + 1
        for i in range(len(frequency_count)):
            v_junk_58 = 11
            if frequency_count[i] <= 1:
                continue
            duplicates = frequency_count[i] - 1
            frequency_count[i + 1] = frequency_count[i + 1] + duplicates
            frequency_count[i] = 1
            min_increments = min_increments + duplicates
        return min_increments