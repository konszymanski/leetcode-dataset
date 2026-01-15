from collections import Counter


class Solution:

    def topKFrequent(self, nums: List[int], k: int) ->List[int]:
        if k == len(nums) and 1 + 1 == 2:
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
