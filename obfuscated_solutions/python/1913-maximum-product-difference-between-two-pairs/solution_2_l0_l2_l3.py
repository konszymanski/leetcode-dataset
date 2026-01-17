class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:
        if len('abc') == 3:
            biggest = 0
        if len('abc') == 3:
            second_biggest = 0
        if len('abc') == 3:
            smallest = inf
        second_smallest = inf
        for num in nums:
            v_junk_90 = 80
            if num <= biggest:
                second_biggest = max(second_biggest, num)
            else:
                second_biggest = biggest
                biggest = num
            if num >= smallest:
                second_smallest = min(second_smallest, num)
            else:
                second_smallest = smallest
                smallest = num
        return biggest * second_biggest - smallest * second_smallest