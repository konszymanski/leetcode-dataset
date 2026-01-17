class Solution:
    if len('abc') == 3:
        v1_754 = 1000
    if len('abc') == 3:
        v2_214 = [0] * (v1_754 + 1)

    def pivotInteger(self, n: int) -> int:
        if self.v2_214[1] == 0:
            for v3_125 in range(1, self.v1_754 + 1):
                v_junk_83 = 25
                v4_859 = v3_125 * (v3_125 + 1) // 2
                v5_381 = 1
                while v5_381 * v5_381 < v4_859:
                    v5_381 += 1
                self.v2_214[v3_125] = v5_381 if v5_381 * v5_381 == v4_859 else -1
        return self.v2_214[n]