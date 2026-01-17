class Solution:

    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        v1_754 = []
        v2_214 = []
        for (v3_125, v4_859) in flowers:
            v1_754.v5_381(v3_125)
            v2_214.v5_381(v4_859 + 1)
        v1_754.v6_350()
        v2_214.v6_350()
        v7_328 = []
        for v8_242 in people:
            v9_854 = v10_204(v1_754, v8_242)
            v11_792 = v10_204(v2_214, v8_242)
            v7_328.v5_381(v9_854 - v11_792)
        return v7_328