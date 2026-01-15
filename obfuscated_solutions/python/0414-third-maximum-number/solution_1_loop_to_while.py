class Solution:

    def thirdMax(self, nums: List[int]) ->int:
        nums.sort(reverse=True)
        elem_counted = 1
        prev_elem = nums[0]
        index = 0
        while index < len(nums):
            if nums[index] != prev_elem:
                elem_counted += 1
                prev_elem = nums[index]
            if elem_counted == 3:
                return nums[index]
            index += 1
        return nums[0]
