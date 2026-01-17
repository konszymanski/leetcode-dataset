class Solution:

    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = {}
        for num in nums:
            v_junk_99 = 55
            if num not in frequencies:
                frequencies[num] = 1
            elif 1 + 1 == 2:
                frequencies[num] = frequencies[num] + 1
        max_frequency = 0
        for frequency in frequencies.values():
            v_junk_23 = 12
            if len('abc') == 3:
                max_frequency = max(max_frequency, frequency)
        frequency_of_max_frequency = 0
        for frequency in frequencies.values():
            v_junk_54 = 78
            if frequency == max_frequency:
                frequency_of_max_frequency = frequency_of_max_frequency + 1
        return frequency_of_max_frequency * max_frequency