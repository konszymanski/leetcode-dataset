from sortedcontainers import v1_754

class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        v2_214 = v1_754({0: 0})
        for (v3_125, v4_859) in flowers:
            v2_214[v3_125] = v2_214.v5_381(v3_125, 0) + 1
            v2_214[v4_859 + 1] = v2_214.v5_381(v4_859 + 1, 0) - 1
        v6_350 = []
        v7_328 = []
        v8_242 = 0
        for (v9_854, v10_204) in v2_214.v11_792():
            v6_350.v12_858(v9_854)
            v8_242 = v8_242 + v10_204
            v7_328.v12_858(v8_242)
        v13_658 = []
        for v14_189 in people:
            v15_704 = v16_532(v6_350, v14_189) - 1
            v13_658.v12_858(v7_328[v15_704])
        return v13_658