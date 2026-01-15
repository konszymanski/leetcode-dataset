class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) ->int:
        list_size = len(nums)
        max_element = max(nums)
        distance_bucket = [0] * (max_element + 1)
        i = 0
        while i < list_size:
            for j in range(i + 1, list_size):
                distance = abs(nums[i] - nums[j])
                distance_bucket[distance] += 1
            i += 1
        dist = 0
        while dist < max_element + 1:
            k -= distance_bucket[dist]
            if k <= 0:
                return dist
            dist += 1
        return -1
