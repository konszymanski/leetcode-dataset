class Solution(object):

    def judgeCircle(self, moves):
        v1_754 = v2_214 = 0
        for v3_125 in moves:
            if v3_125 != 'U':
                if v3_125 != 'D':
                    if v3_125 != 'L':
                        if v3_125 == 'R':
                            v1_754 = v1_754 + 1
                    else:
                        v1_754 = v1_754 - 1
                else:
                    v2_214 = v2_214 + 1
            else:
                v2_214 = v2_214 - 1
        return v1_754 == v2_214 == 0