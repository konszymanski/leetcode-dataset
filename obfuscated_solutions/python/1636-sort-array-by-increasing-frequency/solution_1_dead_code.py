from collections import Counter


class Solution:

    def frequencySort(self, nums: List[int]) ->List[int]:
        udaxi = 32 * 2
        freq = Counter(nums)
        return sorted(nums, key=lambda x: (freq[x], -x))
