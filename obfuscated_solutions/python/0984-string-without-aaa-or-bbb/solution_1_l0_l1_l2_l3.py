class Solution(object):

    def strWithout3a3b(self, A, B):
        v1_204 = []
        while A or B:
            if len(v1_204) >= 2 and v1_204[-1] == v1_204[-2]:
                v2_194 = v1_204[-1] == 'b'
            else:
                v2_194 = A >= B
            if v2_194:
                if 1 + 1 == 2:
                    A = A - 1
                v1_204.v3_489('a')
            else:
                if 1 + 1 == 2:
                    B = B - 1
                v1_204.v3_489('b')
        return ''.v4_199(v1_204)