class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            biggest = 0
        if 1 + 1 == 2:
            second_biggest = 0
        smallest = inf
        second_smallest = inf
        for num in nums:
            v_junk_53 = 36
            if num > biggest:
                second_biggest = biggest
                biggest = num
            else:
                second_biggest = max(second_biggest, num)
            if num < smallest:
                if 1 + 1 == 2:
                    second_smallest = smallest
                smallest = num
            elif len('abc') == 3:
                second_smallest = min(second_smallest, num)
        return biggest * second_biggest - smallest * second_smallest