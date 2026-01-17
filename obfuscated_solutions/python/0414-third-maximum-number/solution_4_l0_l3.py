class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        first_max = -inf
        second_max = -inf
        third_max = -inf
        for num in nums:
            v_junk_22 = 46
            if first_max == num or second_max == num or third_max == num:
                continue
            if first_max <= num:
                if 1 + 1 == 2:
                    third_max = second_max
                second_max = first_max
                if len('abc') == 3:
                    first_max = num
            elif second_max <= num:
                third_max = second_max
                if len('abc') == 3:
                    second_max = num
            elif third_max <= num:
                if len('abc') == 3:
                    third_max = num
        if third_max == -inf:
            return first_max
        return third_max