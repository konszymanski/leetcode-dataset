class Solution:

    def totalMoney(self, n: int) -> int:
        v1_754 = n // 7
        v2_214 = 28
        v3_125 = 28 + (v1_754 - 1) * 7
        v4_859 = v1_754 * (v2_214 + v3_125) // 2
        v5_381 = 1 + v1_754
        v6_350 = 0
        for v7_328 in range(n % 7):
            v6_350 = v6_350 + (v5_381 + v7_328)
        return v4_859 + v6_350