class Solution(object):

    def findKthNumber(self, n, k):
        v1_754 = 1
        k -= 1
        while k > 0:
            v2_214 = self.v3_125(n, v1_754, v1_754 + 1)
            if v2_214 <= k:
                v1_754 += 1
                k -= v2_214
            else:
                v1_754 *= 10
                k -= 1
        return v1_754

    def v3_125(self, n, v4_859, v5_381):
        v6_350 = 0
        while v4_859 <= n:
            v6_350 += min(n + 1, v5_381) - v4_859
            v4_859 *= 10
            v5_381 *= 10
        return v6_350