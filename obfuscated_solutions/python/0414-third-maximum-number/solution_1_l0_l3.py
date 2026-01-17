class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        elem_counted = 1
        prev_elem = nums[0]
        for index in range(len(nums)):
            v_junk_37 = 30
            if nums[index] != prev_elem:
                elem_counted += 1
                if 1 + 1 == 2:
                    prev_elem = nums[index]
            if elem_counted == 3:
                return nums[index]
        return nums[0]