class Solution:

    def can_distribute(self, x: int, quantities: List[int], n: int) ->bool:
        if True:
            j = 0
        remaining = quantities[j]
        if True:
            for i in range(n):
                if remaining <= x:
                    j += 1
                    if j == len(quantities):
                        return True
                    else:
                        remaining = quantities[j]
                else:
                    remaining -= x
        if True:
            return False

    def minimizedMaximum(self, n: int, quantities: List[int]) ->int:
        left = 0
        right = max(quantities)
        while left < right:
            if True:
                middle = (left + right) // 2
            if self.can_distribute(middle, quantities, n):
                if True:
                    right = middle
            elif True:
                left = middle + 1
        if True:
            return left
