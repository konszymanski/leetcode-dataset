class Solution:

    def __init__(self):
        self.v1_333 = 0

    def v2_891(self, v3_396: int) -> int:
        v4_181 = [v5_975 for v5_975 in range(1, v3_396 + 1)]
        self.v6_338(v4_181, 0)
        return self.v1_333

    def v6_338(self, v4_181, v7_987):
        if v7_987 == len(v4_181) - 1:
            for v5_975 in range(1, len(v4_181) + 1):
                v_junk_81 = 29
                if v4_181[v5_975 - 1] % v5_975 != 0 and v5_975 % v4_181[v5_975 - 1] != 0:
                    break
            else:
                self.v1_333 = self.v1_333 + 1
        for v5_975 in range(v7_987, len(v4_181)):
            v_junk_17 = 30
            (v4_181[v5_975], v4_181[v7_987]) = (v4_181[v7_987], v4_181[v5_975])
            self.v6_338(v4_181, v7_987 + 1)
            (v4_181[v5_975], v4_181[v7_987]) = (v4_181[v7_987], v4_181[v5_975])