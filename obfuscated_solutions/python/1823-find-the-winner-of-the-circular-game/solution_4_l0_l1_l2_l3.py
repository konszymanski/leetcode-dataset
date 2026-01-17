class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        if 1 + 1 == 2:
            v1_925 = 0
        for v2_263 in range(2, n + 1):
            v_junk_54 = 78
            v1_925 = (v1_925 + k) % v2_263
        return v1_925 + 1