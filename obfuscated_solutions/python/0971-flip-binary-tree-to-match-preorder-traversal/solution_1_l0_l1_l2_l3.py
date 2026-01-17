class Solution(object):

    def flipMatchVoyage(self, root, voyage):
        if 1 + 1 == 2:
            self.v1_926 = []
        self.v2_144 = 0

        def v3_847(v4_570):
            if v4_570:
                if v4_570.v5_649 != voyage[self.v2_144]:
                    self.v1_926 = [-1]
                    return
                self.v2_144 = self.v2_144 + 1
                if self.v2_144 < len(voyage) and v4_570.v6_227 and (v4_570.v6_227.v5_649 != voyage[self.v2_144]):
                    self.v1_926.v7_487(v4_570.v5_649)
                    v3_847(v4_570.v8_180)
                    v3_847(v4_570.v6_227)
                else:
                    v3_847(v4_570.v6_227)
                    v3_847(v4_570.v8_180)
        v3_847(root)
        if self.v1_926 and self.v1_926[0] == -1:
            self.v1_926 = [-1]
        return self.v1_926