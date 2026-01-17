class Solution:

    def find_max(self, score):
        v1_754 = 0
        for v2_214 in score:
            if v2_214 > v1_754:
                v1_754 = v2_214
        return v1_754

    def v3_125(self, score):
        v4_859 = len(score)
        v5_381 = self.find_max(score)
        v6_350 = [0] * (v5_381 + 1)
        for v7_328 in range(v4_859):
            v6_350[score[v7_328]] = v7_328 + 1
        v8_242 = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        v9_854 = [None] * v4_859
        v10_204 = 1
        for v7_328 in range(v5_381, -1, -1):
            if v6_350[v7_328] != 0:
                v11_792 = v6_350[v7_328] - 1
                if v10_204 >= 4:
                    v9_854[v11_792] = str(v10_204)
                else:
                    v9_854[v11_792] = v8_242[v10_204 - 1]
                v10_204 = v10_204 + 1
        return v9_854