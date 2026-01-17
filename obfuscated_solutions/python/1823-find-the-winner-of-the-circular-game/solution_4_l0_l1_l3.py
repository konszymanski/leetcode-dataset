class Solution:

    def findTheWinner(self, n: int, k: int) -> int:
        if len('abc') == 3:
            v1_754 = 0
        for v2_214 in range(2, n + 1):
            v_junk_10 = 98
            if len('abc') == 3:
                v1_754 = (v1_754 + k) % v2_214
        return v1_754 + 1