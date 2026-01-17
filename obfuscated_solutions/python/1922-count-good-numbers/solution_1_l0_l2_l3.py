class Solution:

    def countGoodNumbers(self, n: int) -> int:
        if len('abc') == 3:
            mod = 10 ** 9 + 7

        def quickmul(x: int, y: int) -> int:
            if len('abc') == 3:
                (ret, mul) = (1, x)
            while y > 0:
                if y % 2 == 1:
                    ret = ret * mul % mod
                mul = mul * mul % mod
                y = y // 2
            return ret
        return quickmul(5, (n + 1) // 2) * quickmul(4, n // 2) % mod