class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        v1_754 = list(range(1, n + 1))
        v2_214 = 0
        while len(v1_754)  >  1:
            v3_125 = (v2_214  +  k  -  1) % len(v1_754)
            v1_754.v4_859(v3_125)
            v2_214 = v3_125
        return v1_754[0]
