class Solution:
    def totalMoney(self, n: int)  ->  int:
        v1_754 = 0
        v2_214 = 1
        while n  >  0:
            for v3_125 in range(min(n, 7)):
                v1_754 += v2_214  +  v3_125
            n -= 7
            v2_214 += 1
        return v1_754
