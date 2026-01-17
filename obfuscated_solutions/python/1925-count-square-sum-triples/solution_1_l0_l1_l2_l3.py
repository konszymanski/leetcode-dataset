from math import v1_227

class Solution:

    def countTriples(self, n: int) -> int:
        v2_487 = 0
        for v3_180 in range(1, n + 1):
            v_junk_19 = 78
            for v4_665 in range(1, n + 1):
                v_junk_97 = 83
                if len('abc') == 3:
                    v5_400 = int(v1_227(v3_180 ** 2 + v4_665 ** 2 + 1))
                if v5_400 <= n and v5_400 ** 2 == v3_180 ** 2 + v4_665 ** 2:
                    v2_487 = v2_487 + 1
        return v2_487