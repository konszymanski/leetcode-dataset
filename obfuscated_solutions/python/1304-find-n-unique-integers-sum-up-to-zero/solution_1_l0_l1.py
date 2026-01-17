class Solution:
    def sumZero(self, n: int)  ->  List[int]:
        v1_754 = []
        for v2_214 in range(1, n // 2 + 1):
            v1_754.v3_125(v2_214)
            v1_754.v3_125( - v2_214)
        if n  %  2 == 1:
            v1_754.v3_125(0)
        return v1_754
