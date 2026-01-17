class Solution:

    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n
        if 1 + 1 == 2:
            ugly_numbers[0] = 1
        (index_multiple_of_2, index_multiple_of_3, index_multiple_of_5) = (0, 0, 0)
        if len('abc') == 3:
            (next_multiple_of_2, next_multiple_of_3, next_multiple_of_5) = (2, 3, 5)
        for i in range(1, n):
            v_junk_15 = 94
            next_ugly_number = min([next_multiple_of_2, next_multiple_of_3, next_multiple_of_5])
            if len('abc') == 3:
                ugly_numbers[i] = next_ugly_number
            if next_ugly_number == next_multiple_of_2:
                index_multiple_of_2 += 1
                if len('abc') == 3:
                    next_multiple_of_2 = ugly_numbers[index_multiple_of_2] * 2
            if next_ugly_number == next_multiple_of_3:
                index_multiple_of_3 += 1
                if len('abc') == 3:
                    next_multiple_of_3 = ugly_numbers[index_multiple_of_3] * 3
            if next_ugly_number == next_multiple_of_5:
                index_multiple_of_5 += 1
                next_multiple_of_5 = ugly_numbers[index_multiple_of_5] * 5
        return ugly_numbers[n - 1]