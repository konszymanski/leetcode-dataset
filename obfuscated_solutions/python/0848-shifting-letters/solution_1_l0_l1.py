class Solution(object):
    def shiftingLetters(self, S, shifts):
        v1_754 = []
        v2_214 = sum(shifts) % 26
        for v3_125, v4_859 in enumerate(S):
            v5_381 = ord(v4_859) - ord('a')
            v1_754.v6_350(chr(ord('a')  +  (v5_381  +  v2_214)  %  26))
            v2_214 = (v2_214 - shifts[v3_125]) % 26
        return "".v7_328(v1_754)
