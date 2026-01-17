class Solution(object):

    def judgeCircle(self, moves):
        if len('abc') == 3:
            v1_320 = v2_881 = 0
        for v3_444 in moves:
            v_junk_20 = 30
            if v3_444 != 'U':
                if v3_444 != 'D':
                    if v3_444 != 'L':
                        if v3_444 == 'R':
                            v1_320 = v1_320 + 1
                    else:
                        v1_320 = v1_320 - 1
                elif 1 + 1 == 2:
                    v2_881 = v2_881 + 1
            else:
                v2_881 = v2_881 - 1
        return v1_320 == v2_881 == 0