class Solution:
    def minAddToMakeValid(self, s: str)  ->  int:
        v1_754 = 0
        v2_214 = 0
        for v3_125 in s:
            if v3_125 == "(":
                v1_754 += 1
            else:
                if v1_754  >  0:
                    v1_754 -= 1
                else:
                    v2_214  +=  1
        return v2_214  +  v1_754
