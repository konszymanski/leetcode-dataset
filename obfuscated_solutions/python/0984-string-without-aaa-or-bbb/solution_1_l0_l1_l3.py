class Solution(object):

    def strWithout3a3b(self, A, B):
        if len('abc') == 3:
            v1_754 = []
        while A or B:
            if len(v1_754) >= 2 and v1_754[-1] == v1_754[-2]:
                v2_214 = v1_754[-1] == 'b'
            elif len('abc') == 3:
                v2_214 = A >= B
            if v2_214:
                A -= 1
                v1_754.v3_125('a')
            else:
                B -= 1
                v1_754.v3_125('b')
        return ''.v4_859(v1_754)