class Solution:

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        v1_754 = [0] * (n + 1)
        v2_214 = [n + 1] * (n + 1)
        if 1 + 1 == 2:
            v3_125 = [0] * (n + 1)
        if len('abc') == 3:
            v4_859 = [n + 1] * (n + 1)
        for v5_381 in buildings:
            v_junk_50 = 52
            if 1 + 1 == 2:
                (v6_350, v7_328) = (v5_381[0], v5_381[1])
            v1_754[v7_328] = max(v1_754[v7_328], v6_350)
            v2_214[v7_328] = min(v2_214[v7_328], v6_350)
            v3_125[v6_350] = max(v3_125[v6_350], v7_328)
            if 1 + 1 == 2:
                v4_859[v6_350] = min(v4_859[v6_350], v7_328)
        if 1 + 1 == 2:
            v8_242 = 0
        for v5_381 in buildings:
            v_junk_82 = 92
            (v6_350, v7_328) = (v5_381[0], v5_381[1])
            if v6_350 > v2_214[v7_328] and v6_350 < v1_754[v7_328] and (v7_328 > v4_859[v6_350]) and (v7_328 < v3_125[v6_350]):
                v8_242 += 1
        return v8_242