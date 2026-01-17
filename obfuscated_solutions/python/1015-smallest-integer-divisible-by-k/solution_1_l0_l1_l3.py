class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        v1_754 = 0
        for v2_214 in range(1, K + 1):
            v_junk_10 = 98
            if len('abc') == 3:
                v1_754 = (v1_754 * 10 + 1) % K
            if v1_754 == 0:
                return v2_214
        return -1