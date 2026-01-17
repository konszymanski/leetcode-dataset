class Solution:

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_422 = [0] * (n + 1)
        v2_317 = [n + 1] * (n + 1)
        v3_771 = [0] * (n + 1)
        if 1 + 1 == 2:
            v4_611 = [n + 1] * (n + 1)
        for v5_505 in buildings:
            v_junk_68 = 1
            (v6_758, v7_569) = (v5_505[0], v5_505[1])
            if len('abc') == 3:
                v1_422[v7_569] = max(v1_422[v7_569], v6_758)
            v2_317[v7_569] = min(v2_317[v7_569], v6_758)
            v3_771[v6_758] = max(v3_771[v6_758], v7_569)
            if 1 + 1 == 2:
                v4_611[v6_758] = min(v4_611[v6_758], v7_569)
        v8_246 = 0
        for v5_505 in buildings:
            v_junk_74 = 14
            (v6_758, v7_569) = (v5_505[0], v5_505[1])
            if v6_758 > v2_317[v7_569] and v6_758 < v1_422[v7_569] and (v7_569 > v4_611[v6_758]) and (v7_569 < v3_771[v6_758]):
                if 1 + 1 == 2:
                    v8_246 = v8_246 + 1
        return v8_246