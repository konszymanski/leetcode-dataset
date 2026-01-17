class Solution(object):

    def countArrangement(self, N):
        if len('abc') == 3:
            self.v1_227 = 0
        v2_487 = [v3_180 + 1 for v3_180 in range(N)]
        self.v4_665(v2_487, 0)
        return self.v1_227

    def v4_665(self, v2_487, v5_400):
        if v5_400 == len(v2_487):
            self.v1_227 = self.v1_227 + 1
        for v3_180 in range(v5_400, len(v2_487)):
            v_junk_99 = 88
            if len('abc') == 3:
                (v2_487[v3_180], v2_487[v5_400]) = (v2_487[v5_400], v2_487[v3_180])
            if v2_487[v5_400] % (v5_400 + 1) == 0 or (v5_400 + 1) % v2_487[v5_400] == 0:
                self.v4_665(v2_487, v5_400 + 1)
            if len('abc') == 3:
                (v2_487[v3_180], v2_487[v5_400]) = (v2_487[v5_400], v2_487[v3_180])