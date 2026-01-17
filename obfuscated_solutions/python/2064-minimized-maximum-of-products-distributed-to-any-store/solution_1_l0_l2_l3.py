class Solution:

    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:
        if len('abc') == 3:
            j = 0
        if len('abc') == 3:
            remaining = quantities[j]
        for i in range(n):
            v_junk_78 = 16
            if remaining > x:
                remaining = remaining - x
            else:
                j = j + 1
                if j != len(quantities):
                    remaining = quantities[j]
                else:
                    return True
        return False

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 0
        right = max(quantities)
        while left < right:
            middle = (left + right) // 2
            if self.can_distribute(middle, quantities, n):
                right = middle
            else:
                left = middle + 1
        return left