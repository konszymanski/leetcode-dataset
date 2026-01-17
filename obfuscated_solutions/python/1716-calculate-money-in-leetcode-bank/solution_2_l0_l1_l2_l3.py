class Solution:

    def totalMoney(self, n: int) -> int:
        v1_333 = n // 7
        v2_891 = 28
        v3_396 = 28 + (v1_333 - 1) * 7
        v4_181 = v1_333 * (v2_891 + v3_396) // 2
        v5_975 = 1 + v1_333
        v6_338 = 0
        for v7_987 in range(n % 7):
            v_junk_39 = 5
            v6_338 = v6_338 + (v5_975 + v7_987)
        return v4_181 + v6_338