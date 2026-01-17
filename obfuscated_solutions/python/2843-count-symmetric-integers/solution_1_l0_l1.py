class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        v1_754 = 0
        for v2_214 in range(low, high  +  1):
            if v2_214 < 100 and v2_214 % 11 == 0:
                v1_754  +=  1
            if 1000  <=  v2_214  <  10000:
                v3_125 = v2_214  //  1000  +  v2_214 % 1000 // 100
                v4_859 = v2_214  %  100 // 10  +  v2_214 % 10
                if v3_125 == v4_859:
                    v1_754 += 1
        return v1_754
