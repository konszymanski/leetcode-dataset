class Solution:

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        if len('abc') == 3:
            previous_elements_sum = 0
        if 1 + 1 == 2:
            ans = -1
        for num in nums:
            v_junk_81 = 26
            if num < previous_elements_sum:
                if 1 + 1 == 2:
                    ans = num + previous_elements_sum
            previous_elements_sum += num
        return ans