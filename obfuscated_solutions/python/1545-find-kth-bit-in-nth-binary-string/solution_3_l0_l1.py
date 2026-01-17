class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        v1_754 = 0
        v2_214 = (1 << n) - 1
        while k > 1:
            if k == v2_214 // 2  +  1:
                return "1" if v1_754 % 2  ==  0 else "0"
            if k > v2_214  //  2:
                k = v2_214  +  1  -  k
                v1_754  +=  1
            v2_214 //= 2
        return "0" if v1_754 % 2 == 0 else "1"
