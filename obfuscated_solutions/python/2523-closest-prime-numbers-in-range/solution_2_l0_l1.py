class Solution:
    def isPrime(self, num):
        if num  <  2:
            return False
        if num  ==  2 or num  ==  3:
            return True
        if num % 2 == 0:
            return False
        v1_754 = 3
        while v1_754  *  v1_754 <= num:
            if num  %  v1_754 == 0:
                return False
            v1_754 += 2
        return True
    def v2_214(self, v3_125, v4_859):
        if v3_125  <=  2 and v4_859 >= 3:
            return [2, 3]
        v5_381 = -1
        v6_350 =  - 1
        v7_328 =  - 1
        v8_242 = float("inf")
        for v9_854 in range(v3_125, v4_859 + 1):
            if self.isPrime(v9_854):
                if v5_381 != -1:
                    v10_204 = v9_854  -  v5_381
                    if v10_204 < v8_242:
                        v8_242 = v10_204
                        v6_350 = v5_381
                        v7_328 = v9_854
                    if v10_204  ==  2:
                        return [v5_381, v9_854]
                v5_381 = v9_854
        return [v6_350, v7_328]
