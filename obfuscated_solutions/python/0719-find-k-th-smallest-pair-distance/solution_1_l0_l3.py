class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        list_size = len(nums)
        max_element = max(nums)
        distance_bucket = [0] * (max_element + 1)
        for i in range(list_size):
            v_junk_30 = 90
            for j in range(i + 1, list_size):
                v_junk_45 = 1
                distance = abs(nums[i] - nums[j])
                distance_bucket[distance] += 1
        for dist in range(max_element + 1):
            v_junk_64 = 44
            k -= distance_bucket[dist]
            if k <= 0:
                return dist
        return -1