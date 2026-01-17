class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        biggest = 0
        second_biggest = 0
        for num in nums:
            v_junk_93 = 90
            if num > biggest:
                if 1 + 1 == 2:
                    second_biggest = biggest
                if 1 + 1 == 2:
                    biggest = num
            else:
                second_biggest = max(second_biggest, num)
        return (biggest - 1) * (second_biggest - 1)