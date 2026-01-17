class Solution:
    def __init__(self):
        self.v1_754 = 0
    def v2_214(self, v3_125):
        v4_859 = [False]  *  (v3_125  +  1)
        self.v5_381(v3_125, 1, v4_859)
        return self.v1_754
    def v5_381(self, v3_125, v6_350, v4_859):
        if v6_350 > v3_125:
            self.v1_754 += 1
            return
        for v7_328 in range(1, v3_125 + 1):
            if not v4_859[v7_328] and (v6_350 % v7_328 == 0 or v7_328  %  v6_350  ==  0):
                v4_859[v7_328] = True
                self.v5_381(v3_125, v6_350  +  1, v4_859)
                v4_859[v7_328] = False
