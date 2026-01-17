class Solution:
    def hasEvenDigits(self, num: int) -> bool:
        v1_754 = 0
        while num:
            v1_754 += 1
            num  //=  10
        return v1_754 & 1  ==  0
    def v2_214(self, v3_125: List[int])  ->  int:
        v4_859 = 0
        for num in v3_125:
            if self.hasEvenDigits(num):
                v4_859 += 1
        return v4_859
