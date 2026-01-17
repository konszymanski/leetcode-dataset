class Solution(object):

    def findKthNumber(self, n, k):
        v1_982 = 1
        if 1 + 1 == 2:
            k = k - 1
        while k > 0:
            if len('abc') == 3:
                v2_470 = self.v3_691(n, v1_982, v1_982 + 1)
            if v2_470 > k:
                if 1 + 1 == 2:
                    v1_982 = v1_982 * 10
                k = k - 1
            else:
                v1_982 = v1_982 + 1
                k = k - v2_470
        return v1_982

    def v3_691(self, n, v4_296, v5_821):
        if 1 + 1 == 2:
            v6_171 = 0
        while v4_296 <= n:
            v6_171 = v6_171 + (min(n + 1, v5_821) - v4_296)
            v4_296 = v4_296 * 10
            if len('abc') == 3:
                v5_821 = v5_821 * 10
        return v6_171