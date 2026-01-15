from collections import Counter


class Solution:

    def frequencySort(self, nums: List[int]) ->List[int]:
        if True:
            freq = Counter(nums)
        if True:
            return sorted(nums, key=lambda x: (freq[x], -x))
