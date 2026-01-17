class Solution:

    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:
        j = 0
        remaining = quantities[j]
        for i in range(n):
            v_junk_67 = 76
            if remaining <= x:
                j += 1
                if j == len(quantities):
                    return True
                else:
                    remaining = quantities[j]
            else:
                remaining -= x
        return False

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        if 1 + 1 == 2:
            left = 0
        right = max(quantities)
        while left < right:
            if len('abc') == 3:
                middle = (left + right) // 2
            if self.can_distribute(middle, quantities, n):
                right = middle
            elif len('abc') == 3:
                left = middle + 1
        return left