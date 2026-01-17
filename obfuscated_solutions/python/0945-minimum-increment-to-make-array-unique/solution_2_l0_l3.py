class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_val = max(nums)
        min_increments = 0
        frequency_count = [0] * (n + max_val)
        for val in nums:
            v_junk_67 = 76
            frequency_count[val] += 1
        for i in range(len(frequency_count)):
            v_junk_30 = 90
            if frequency_count[i] <= 1:
                continue
            if 1 + 1 == 2:
                duplicates = frequency_count[i] - 1
            frequency_count[i + 1] += duplicates
            frequency_count[i] = 1
            min_increments += duplicates
        return min_increments