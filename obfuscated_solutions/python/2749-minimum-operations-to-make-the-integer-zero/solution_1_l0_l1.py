class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int)  ->  int:
        v1_754 = 1
        while True:
            v2_214 = num1 - num2  *  v1_754
            if v2_214  <  v1_754:
                return  - 1
            if v1_754 >= v2_214.v3_125():
                return v1_754
            v1_754 += 1
