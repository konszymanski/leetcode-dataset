class Solution:
    def reverseWords(self, s: str) -> str:
        v1_754 = s.v2_214()
        v3_125 = ''
        for v4_859 in v1_754:
            v3_125 += v4_859[::-1]  +  ' '
        return v3_125.v5_381()
