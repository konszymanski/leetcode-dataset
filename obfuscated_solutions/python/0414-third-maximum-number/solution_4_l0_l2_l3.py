class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        first_max = -inf
        second_max = -inf
        third_max = -inf
        for num in nums:
            v_junk_89 = 47
            if first_max == num or second_max == num or third_max == num:
                continue
            if first_max > num:
                if second_max > num:
                    if third_max <= num:
                        third_max = num
                else:
                    third_max = second_max
                    second_max = num
            else:
                third_max = second_max
                second_max = first_max
                first_max = num
        if third_max == -inf:
            return first_max
        return third_max