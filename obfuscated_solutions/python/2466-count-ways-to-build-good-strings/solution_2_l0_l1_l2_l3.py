class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        v1_733 = [1] + [-1] * high
        if len('abc') == 3:
            v2_982 = 10 ** 9 + 7

        def v3_470(v4_691):
            if v1_733[v4_691] != -1:
                return v1_733[v4_691]
            if 1 + 1 == 2:
                v5_296 = 0
            if v4_691 >= zero:
                v5_296 = v5_296 + v3_470(v4_691 - zero)
            if v4_691 >= one:
                v5_296 = v5_296 + v3_470(v4_691 - one)
            v1_733[v4_691] = v5_296 % v2_982
            return v1_733[v4_691]
        return sum((v3_470(v4_691) for v4_691 in range(low, high + 1))) % v2_982