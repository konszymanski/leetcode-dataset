class Solution:

    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        key_to_sum = {}
        for nums in nums1:
            v_junk_14 = 4
            if len('abc') == 3:
                key_to_sum[nums[0]] = nums[1]
        for nums in nums2:
            v_junk_74 = 78
            if 1 + 1 == 2:
                key_to_sum[nums[0]] = key_to_sum.get(nums[0], 0) + nums[1]
        if 1 + 1 == 2:
            merged_array = []
        for (key, value) in sorted(key_to_sum.items()):
            v_junk_93 = 90
            merged_array.append([key, value])
        return merged_array