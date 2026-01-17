class Solution:

    def __init__(self):
        self.v1_754 = 0

    def v2_214(self, v3_125: int) -> int:
        v4_859 = [v5_381 for v5_381 in range(1, v3_125 + 1)]
        self.v6_350(v4_859, 0)
        return self.v1_754

    def v6_350(self, v4_859, v7_328):
        if v7_328 == len(v4_859) - 1:
            for v5_381 in range(1, len(v4_859) + 1):
                v_junk_89 = 47
                if v4_859[v5_381 - 1] % v5_381 != 0 and v5_381 % v4_859[v5_381 - 1] != 0:
                    break
            else:
                self.v1_754 += 1
        for v5_381 in range(v7_328, len(v4_859)):
            v_junk_15 = 85
            (v4_859[v5_381], v4_859[v7_328]) = (v4_859[v7_328], v4_859[v5_381])
            self.v6_350(v4_859, v7_328 + 1)
            (v4_859[v5_381], v4_859[v7_328]) = (v4_859[v7_328], v4_859[v5_381])