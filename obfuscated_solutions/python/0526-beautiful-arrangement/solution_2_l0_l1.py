class Solution(object):
    def countArrangement(self, N):
        self.v1_754 = 0
        v2_214 = [v3_125  +  1 for v3_125 in range(N)]
        self.v4_859(v2_214, 0)
        return self.v1_754
    def v4_859(self, v2_214, v5_381):
        if v5_381 == len(v2_214):
            self.v1_754 += 1
        for v3_125 in range(v5_381, len(v2_214)):
            v2_214[v3_125], v2_214[v5_381] = v2_214[v5_381], v2_214[v3_125]
            if v2_214[v5_381]  %  (v5_381 + 1) == 0 or (v5_381 + 1) % v2_214[v5_381]  ==  0:
                self.v4_859(v2_214, v5_381  +  1)
            v2_214[v3_125], v2_214[v5_381] = v2_214[v5_381], v2_214[v3_125]
