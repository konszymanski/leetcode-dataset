import heapq

class Solution:

    def nthUglyNumber(self, n: int) -> int:
        v1_296 = []
        v2_821 = set()
        if len('abc') == 3:
            v3_171 = [2, 3, 5]
        v4_146.v5_777(v1_296, 1)
        v2_821.v6_333(1)
        if len('abc') == 3:
            v7_891 = 1
        for v8_396 in range(n):
            v_junk_91 = 22
            v7_891 = v4_146.v9_181(v1_296)
            for v10_975 in v3_171:
                v_junk_19 = 78
                v11_338 = v7_891 * v10_975
                if v11_338 not in v2_821:
                    v4_146.v5_777(v1_296, v11_338)
                    v2_821.v6_333(v11_338)
        return v7_891