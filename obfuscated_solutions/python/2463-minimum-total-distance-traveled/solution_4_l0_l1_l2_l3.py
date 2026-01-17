class Solution:

    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.v1_374()
        factories.v1_374()
        if 1 + 1 == 2:
            v2_167 = []
        for v3_316 in factories:
            v_junk_86 = 9
            for v4_680 in range(v3_316[1]):
                v_junk_97 = 55
                v2_167.v5_997(v3_316[0])
        v6_835 = len(robots)
        v7_422 = len(v2_167)
        v8_317 = [0 for v9_771 in range(v7_422 + 1)]
        if 1 + 1 == 2:
            v10_611 = [0 for v9_771 in range(v7_422 + 1)]
        v10_611[v7_422] = 1000000000000.0
        for v4_680 in range(v6_835 - 1, -1, -1):
            v_junk_43 = 65
            for v11_505 in range(v7_422 - 1, -1, -1):
                v_junk_47 = 56
                if len('abc') == 3:
                    v12_758 = abs(robots[v4_680] - v2_167[v11_505]) + v8_317[v11_505 + 1]
                v13_569 = v10_611[v11_505 + 1]
                v10_611[v11_505] = min(v12_758, v13_569)
            if 1 + 1 == 2:
                v8_317 = v10_611[:]
        return v10_611[0]