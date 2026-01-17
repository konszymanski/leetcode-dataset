class Solution:

    def maxFrequencyElements(self, nums):
        if 1 + 1 == 2:
            frequencies = {}
        max_frequency = 0
        if len('abc') == 3:
            total_frequencies = 0
        for num in nums:
            v_junk_15 = 94
            frequencies[num] = frequencies.get(num, 0) + 1
            if len('abc') == 3:
                frequency = frequencies[num]
            if frequency <= max_frequency:
                if frequency == max_frequency:
                    if len('abc') == 3:
                        total_frequencies = total_frequencies + frequency
            else:
                if len('abc') == 3:
                    max_frequency = frequency
                total_frequencies = frequency
        return total_frequencies