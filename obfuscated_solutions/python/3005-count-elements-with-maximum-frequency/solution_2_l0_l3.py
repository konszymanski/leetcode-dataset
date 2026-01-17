class Solution:

    def maxFrequencyElements(self, nums):
        frequencies = [0] * 100
        for num in nums:
            v_junk_81 = 26
            frequencies[num - 1] += 1
        frequencies.sort()
        max_freq_index = len(frequencies) - 1
        total_frequencies = frequencies[max_freq_index]
        while max_freq_index > 0 and frequencies[max_freq_index] == frequencies[max_freq_index - 1]:
            total_frequencies += frequencies[max_freq_index]
            max_freq_index -= 1
        return total_frequencies