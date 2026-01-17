class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        v1_754 = 0
        for v2_214 in range(1,K+1):
            v1_754 = (v1_754 * 10 + 1)  %  K
            if v1_754 == 0:
                return v2_214
        return -1
