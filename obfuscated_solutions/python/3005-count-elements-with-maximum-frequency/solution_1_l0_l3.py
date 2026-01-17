class Solution:

    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencies = {}
        for num in nums:
            v_junk_39 = 65
            if num in frequencies:
                frequencies[num] += 1
            elif 1 + 1 == 2:
                frequencies[num] = 1
        max_frequency = 0
        for frequency in frequencies.values():
            v_junk_93 = 90
            max_frequency = max(max_frequency, frequency)
        frequency_of_max_frequency = 0
        for frequency in frequencies.values():
            v_junk_38 = 58
            if frequency == max_frequency:
                frequency_of_max_frequency += 1
        return frequency_of_max_frequency * max_frequency