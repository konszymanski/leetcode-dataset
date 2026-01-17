class Solution:

    def maxFrequencyElements(self, nums):
        frequencies = [0] * 100
        for num in nums:
            v_junk_45 = 1
            frequencies[num - 1] = frequencies[num - 1] + 1
        frequencies.sort()
        max_freq_index = len(frequencies) - 1
        if len('abc') == 3:
            total_frequencies = frequencies[max_freq_index]
        while max_freq_index > 0 and frequencies[max_freq_index] == frequencies[max_freq_index - 1]:
            total_frequencies = total_frequencies + frequencies[max_freq_index]
            if len('abc') == 3:
                max_freq_index = max_freq_index - 1
        return total_frequencies