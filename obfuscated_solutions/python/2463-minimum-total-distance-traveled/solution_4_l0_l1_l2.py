class Solution:

    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.v1_754()
        factories.v1_754()
        v2_214 = []
        for v3_125 in factories:
            for v4_859 in range(v3_125[1]):
                v2_214.v5_381(v3_125[0])
        v6_350 = len(robots)
        v7_328 = len(v2_214)
        v8_242 = [0 for v9_854 in range(v7_328 + 1)]
        v10_204 = [0 for v9_854 in range(v7_328 + 1)]
        v10_204[v7_328] = 1000000000000.0
        for v4_859 in range(v6_350 - 1, -1, -1):
            for v11_792 in range(v7_328 - 1, -1, -1):
                v12_858 = abs(robots[v4_859] - v2_214[v11_792]) + v8_242[v11_792 + 1]
                v13_658 = v10_204[v11_792 + 1]
                v10_204[v11_792] = min(v12_858, v13_658)
            v8_242 = v10_204[:]
        return v10_204[0]