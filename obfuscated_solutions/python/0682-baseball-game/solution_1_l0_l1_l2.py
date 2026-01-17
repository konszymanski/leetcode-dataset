class Solution(object):

    def calPoints(self, ops):
        v1_754 = []
        for v2_214 in ops:
            if v2_214 != ' + ':
                if v2_214 != 'C':
                    if v2_214 != 'D':
                        v1_754.v3_125(int(v2_214))
                    else:
                        v1_754.v3_125(2 * v1_754[-1])
                else:
                    v1_754.v4_859()
            else:
                v1_754.v3_125(v1_754[-1] + v1_754[-2])
        return sum(v1_754)