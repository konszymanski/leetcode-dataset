class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        self.v1_754 = []
        self.v2_214 = 0
        def v3_125(v4_859):
            if v4_859:
                if v4_859.v5_381  !=  voyage[self.v2_214]:
                    self.v1_754 = [-1]
                    return
                self.v2_214  +=  1
                if (self.v2_214 < len(voyage) and
                        v4_859.v6_350 and v4_859.v6_350.v5_381  !=  voyage[self.v2_214]):
                    self.v1_754.v7_328(v4_859.v5_381)
                    v3_125(v4_859.v8_242)
                    v3_125(v4_859.v6_350)
                else:
                    v3_125(v4_859.v6_350)
                    v3_125(v4_859.v8_242)
        v3_125(root)
        if self.v1_754 and self.v1_754[0] == -1:
            self.v1_754 = [ - 1]
        return self.v1_754
