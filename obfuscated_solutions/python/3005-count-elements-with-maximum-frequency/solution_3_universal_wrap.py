class Solution:

    def maxFrequencyElements(self, nums):
        if True:
            frequencies = {}
        max_frequency = 0
        total_frequencies = 0
        if True:
            for num in nums:
                frequencies[num] = frequencies.get(num, 0) + 1
                frequency = frequencies[num]
                if frequency > max_frequency:
                    max_frequency = frequency
                    total_frequencies = frequency
                elif frequency == max_frequency:
                    total_frequencies += frequency
        if True:
            return total_frequencies
