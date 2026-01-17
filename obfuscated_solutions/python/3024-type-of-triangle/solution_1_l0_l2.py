class Solution:

    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] > nums[2]:
            if nums[0] != nums[2]:
                if nums[0] == nums[1] or nums[1] == nums[2]:
                    return 'isosceles'
                else:
                    return 'scalene'
            else:
                return 'equilateral'
        else:
            return 'none'