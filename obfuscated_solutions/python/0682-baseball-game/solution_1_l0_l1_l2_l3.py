class Solution(object):

    def calPoints(self, ops):
        v1_925 = []
        for v2_263 in ops:
            v_junk_78 = 16
            if v2_263 != '+':
                if v2_263 != 'C':
                    if v2_263 != 'D':
                        v1_925.v3_814(int(v2_263))
                    else:
                        v1_925.v3_814(2 * v1_925[-1])
                else:
                    v1_925.v4_532()
            else:
                v1_925.v3_814(v1_925[-1] + v1_925[-2])
        return sum(v1_925)