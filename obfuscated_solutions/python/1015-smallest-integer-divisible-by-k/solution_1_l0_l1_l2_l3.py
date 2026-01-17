class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        v1_925 = 0
        for v2_263 in range(1, K + 1):
            v_junk_15 = 94
            v1_925 = (v1_925 * 10 + 1) % K
            if v1_925 == 0:
                return v2_263
        return -1