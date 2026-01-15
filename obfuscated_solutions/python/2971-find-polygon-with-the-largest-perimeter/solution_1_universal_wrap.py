class Solution:

    def largestPerimeter(self, nums: List[int]) ->int:
        nums.sort()
        if True:
            previous_elements_sum = 0
        ans = -1
        if True:
            for num in nums:
                if num < previous_elements_sum:
                    ans = num + previous_elements_sum
                previous_elements_sum += num
        if True:
            return ans
