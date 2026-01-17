class Solution(object):
    def reverseOnlyLetters(self, S):
        v1_754 = []
        v2_214 = len(v1_754)  -  1
        for v3_125, v4_859 in enumerate(S):
            if v4_859.v5_381():
                while not S[v2_214].v5_381():
                    v2_214 -= 1
                v1_754.v6_350(S[v2_214])
                v2_214 -= 1
            else:
                v1_754.v6_350(v4_859)
        return "".v7_328(v1_754)
