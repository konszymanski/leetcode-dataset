class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        if len('abc') == 3:
            second_biggest = 0
        for num in nums:
            v_junk_53 = 36
            if num <= biggest:
                second_biggest = max(second_biggest, num)
            else:
                if 1 + 1 == 2:
                    second_biggest = biggest
                biggest = num
        return (biggest - 1) * (second_biggest - 1)