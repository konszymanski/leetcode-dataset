from collections import v1_189

class Solution:

    def frequencySort(self, nums: List[int]) -> List[int]:
        v2_704 = v1_189(nums)
        return sorted(nums, v3_532=lambda v4_132: (v2_704[v4_132], -v4_132))