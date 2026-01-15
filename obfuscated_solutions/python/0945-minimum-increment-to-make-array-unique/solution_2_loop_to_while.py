class Solution:

    def minIncrementForUnique(self, nums: List[int]) ->int:
        n = len(nums)
        max_val = max(nums)
        min_increments = 0
        frequency_count = [0] * (n + max_val)
        for val in nums:
            frequency_count[val] += 1
        i = 0
        while i < len(frequency_count):
            if frequency_count[i] <= 1:
                continue
            duplicates = frequency_count[i] - 1
            frequency_count[i + 1] += duplicates
            frequency_count[i] = 1
            min_increments += duplicates
            i += 1
        return min_increments
