class Solution:
    v1_821 = 1000
    if len('abc') == 3:
        v2_171 = [0] * (v1_821 + 1)

    def pivotInteger(self, n: int) -> int:
        if self.v2_171[1] == 0:
            for v3_146 in range(1, self.v1_821 + 1):
                v_junk_97 = 42
                v4_777 = v3_146 * (v3_146 + 1) // 2
                v5_333 = 1
                while v5_333 * v5_333 < v4_777:
                    v5_333 = v5_333 + 1
                self.v2_171[v3_146] = v5_333 if v5_333 * v5_333 == v4_777 else -1
        return self.v2_171[n]