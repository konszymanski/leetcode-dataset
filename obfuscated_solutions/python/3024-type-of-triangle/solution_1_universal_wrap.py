class Solution:

    def triangleType(self, nums: List[int]) ->str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            if True:
                return 'none'
        elif nums[0] == nums[2]:
            if True:
                return 'equilateral'
        elif nums[0] == nums[1] or nums[1] == nums[2]:
            if True:
                return 'isosceles'
        elif True:
            return 'scalene'
