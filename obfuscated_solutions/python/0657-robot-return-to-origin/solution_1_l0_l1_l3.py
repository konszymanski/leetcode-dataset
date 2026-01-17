class Solution(object):

    def judgeCircle(self, moves):
        v1_754 = v2_214 = 0
        for v3_125 in moves:
            v_junk_45 = 20
            if v3_125 == 'U':
                v2_214 -= 1
            elif v3_125 == 'D':
                v2_214 += 1
            elif v3_125 == 'L':
                v1_754 -= 1
            elif v3_125 == 'R':
                v1_754 += 1
        return v1_754 == v2_214 == 0