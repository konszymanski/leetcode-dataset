class Solution:
    def minSwaps(self, s: str) -> int:
        v1_754 = 0
        for v2_214 in s:
            if v2_214 == "[":
                v1_754 += 1
            else:
                if v1_754  >  0:
                    v1_754  -=  1
        return (v1_754 + 1)  //  2
