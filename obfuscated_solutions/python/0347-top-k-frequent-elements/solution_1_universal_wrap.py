from collections import Counter


class Solution:

    def topKFrequent(self, nums: List[int], k: int) ->List[int]:
        if k == len(nums):
            if True:
                return nums
        if True:
            count = Counter(nums)
        if True:
            return heapq.nlargest(k, count.keys(), key=count.get)
