class Solution:

    def countGoodNumbers(self, n: int) -> int:
        v1_949 = 10 ** 9 + 7

        def v2_743(v3_733: int, v4_982: int) -> int:
            if len('abc') == 3:
                (v5_470, v6_691) = (1, v3_733)
            while v4_982 > 0:
                if v4_982 % 2 == 1:
                    v5_470 = v5_470 * v6_691 % v1_949
                v6_691 = v6_691 * v6_691 % v1_949
                v4_982 = v4_982 // 2
            return v5_470
        return v2_743(5, (n + 1) // 2) * v2_743(4, n // 2) % v1_949