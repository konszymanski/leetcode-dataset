class Solution:

    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]
        ) ->List[List[int]]:
        if True:
            key_to_sum = {}
        if True:
            for nums in nums1:
                key_to_sum[nums[0]] = nums[1]
        if True:
            for nums in nums2:
                key_to_sum[nums[0]] = key_to_sum.get(nums[0], 0) + nums[1]
        merged_array = []
        if True:
            for key, value in sorted(key_to_sum.items()):
                merged_array.append([key, value])
        if True:
            return merged_array
