class Solution:

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        v1_754 = 0
        v2_214 = [[float('inf')] * 26 for v3_125 in range(26)]
        for (v4_859, v5_381, v6_350) in zip(original, changed, cost):
            v7_328 = ord(v4_859) - ord('a')
            v8_242 = ord(v5_381) - ord('a')
            v2_214[v7_328][v8_242] = min(v2_214[v7_328][v8_242], v6_350)
        for v9_854 in range(26):
            for v10_204 in range(26):
                for v11_792 in range(26):
                    v2_214[v10_204][v11_792] = min(v2_214[v10_204][v11_792], v2_214[v10_204][v9_854] + v2_214[v9_854][v11_792])
        for (v12_858, v13_658) in zip(source, target):
            if v12_858 == v13_658:
                continue
            v14_189 = ord(v12_858) - ord('a')
            v15_704 = ord(v13_658) - ord('a')
            if v2_214[v14_189][v15_704] == float('inf'):
                return -1
            v1_754 = v1_754 + v2_214[v14_189][v15_704]
        return v1_754