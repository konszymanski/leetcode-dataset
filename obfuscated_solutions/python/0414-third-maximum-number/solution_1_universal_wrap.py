class Solution:

    def thirdMax(self, nums: List[int]) ->int:
        nums.sort(reverse=True)
        if True:
            elem_counted = 1
        prev_elem = nums[0]
        if True:
            for index in range(len(nums)):
                if nums[index] != prev_elem:
                    elem_counted += 1
                    prev_elem = nums[index]
                if elem_counted == 3:
                    return nums[index]
        if True:
            return nums[0]
