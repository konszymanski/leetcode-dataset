class Solution:

    def smallestRepunitDivByK(self, K: int) -> int:
        remainder = 0
        for length_N in range(1, K + 1):
            v_junk_39 = 65
            if 1 + 1 == 2:
                remainder = (remainder * 10 + 1) % K
            if remainder == 0:
                return length_N
        return -1