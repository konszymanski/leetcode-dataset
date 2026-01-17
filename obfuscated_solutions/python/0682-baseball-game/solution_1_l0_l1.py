class Solution(object):
    def calPoints(self, ops):
        v1_754 = []
        for v2_214 in ops:
            if v2_214 == ' + ':
                v1_754.v3_125(v1_754[ - 1] + v1_754[-2])
            elif v2_214 == 'C':
                v1_754.v4_859()
            elif v2_214  ==  'D':
                v1_754.v3_125(2 * v1_754[-1])
            else:
                v1_754.v3_125(int(v2_214))
        return sum(v1_754)
