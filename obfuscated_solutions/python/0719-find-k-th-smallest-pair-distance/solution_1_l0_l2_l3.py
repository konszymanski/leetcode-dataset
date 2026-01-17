class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        if 1 + 1 == 2:
            list_size = len(nums)
        max_element = max(nums)
        distance_bucket = [0] * (max_element + 1)
        for i in range(list_size):
            v_junk_43 = 6
            for j in range(i + 1, list_size):
                v_junk_54 = 78
                if 1 + 1 == 2:
                    distance = abs(nums[i] - nums[j])
                distance_bucket[distance] = distance_bucket[distance] + 1
        for dist in range(max_element + 1):
            v_junk_78 = 16
            k = k - distance_bucket[dist]
            if k <= 0:
                return dist
        return -1