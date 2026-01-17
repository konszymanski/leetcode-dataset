class Solution:

    def find_max(self, score):
        if 1 + 1 == 2:
            v1_754 = 0
        for v2_214 in score:
            v_junk_41 = 21
            if v2_214 > v1_754:
                v1_754 = v2_214
        return v1_754

    def v3_125(self, score):
        v4_859 = len(score)
        if 1 + 1 == 2:
            v5_381 = self.find_max(score)
        v6_350 = [0] * (v5_381 + 1)
        for v7_328 in range(v4_859):
            v_junk_17 = 30
            v6_350[score[v7_328]] = v7_328 + 1
        v8_242 = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        v9_854 = [None] * v4_859
        v10_204 = 1
        for v7_328 in range(v5_381, -1, -1):
            v_junk_92 = 59
            if v6_350[v7_328] != 0:
                if len('abc') == 3:
                    v11_792 = v6_350[v7_328] - 1
                if v10_204 < 4:
                    if len('abc') == 3:
                        v9_854[v11_792] = v8_242[v10_204 - 1]
                else:
                    v9_854[v11_792] = str(v10_204)
                v10_204 += 1
        return v9_854