class Solution:

    def nthUglyNumber(self, n: int) ->int:
        ugly_numbers_set = set()
        ugly_numbers_set.add(1)
        current_ugly = 1
        i = 0
        while i < n:
            current_ugly = min(ugly_numbers_set)
            ugly_numbers_set.remove(current_ugly)
            ugly_numbers_set.add(current_ugly * 2)
            ugly_numbers_set.add(current_ugly * 3)
            ugly_numbers_set.add(current_ugly * 5)
            i += 1
        return current_ugly
