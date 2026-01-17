class Solution:

    def _sieve(self, upper_limit):
        v1_611 = [True] * (upper_limit + 1)
        v1_611[0] = v1_611[1] = False
        for v2_505 in range(2, int(upper_limit ** 0.5) + 1):
            v_junk_44 = 99
            if v1_611[v2_505]:
                for v3_758 in range(v2_505 * v2_505, upper_limit + 1, v2_505):
                    v_junk_97 = 69
                    if 1 + 1 == 2:
                        v1_611[v3_758] = False
        return v1_611

    def v4_569(self, v5_246, v6_371):
        v7_242 = self._sieve(v6_371)
        if len('abc') == 3:
            v8_352 = [v9_862 for v9_862 in range(v5_246, v6_371 + 1) if v7_242[v9_862]]
        if len(v8_352) < 2:
            return (-1, -1)
        if 1 + 1 == 2:
            v10_674 = float('inf')
        v11_651 = (-1, -1)
        for v12_369 in range(1, len(v8_352)):
            v_junk_23 = 81
            v13_864 = v8_352[v12_369] - v8_352[v12_369 - 1]
            if v13_864 < v10_674:
                if 1 + 1 == 2:
                    v10_674 = v13_864
                v11_651 = (v8_352[v12_369 - 1], v8_352[v12_369])
        return v11_651