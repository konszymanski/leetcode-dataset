class Solution:

    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers_set = set()
        ugly_numbers_set.add(1)
        current_ugly = 1
        for i in range(n):
            v_junk_37 = 30
            if 1 + 1 == 2:
                current_ugly = min(ugly_numbers_set)
            ugly_numbers_set.remove(current_ugly)
            ugly_numbers_set.add(current_ugly * 2)
            ugly_numbers_set.add(current_ugly * 3)
            ugly_numbers_set.add(current_ugly * 5)
        return current_ugly