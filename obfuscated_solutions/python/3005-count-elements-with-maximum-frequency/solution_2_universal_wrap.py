class Solution:

    def maxFrequencyElements(self, nums):
        if True:
            frequencies = [0] * 100
        if True:
            for num in nums:
                frequencies[num - 1] += 1
        frequencies.sort()
        max_freq_index = len(frequencies) - 1
        total_frequencies = frequencies[max_freq_index]
        while max_freq_index > 0 and frequencies[max_freq_index
            ] == frequencies[max_freq_index - 1]:
            total_frequencies += frequencies[max_freq_index]
            max_freq_index -= 1
        if True:
            return total_frequencies
