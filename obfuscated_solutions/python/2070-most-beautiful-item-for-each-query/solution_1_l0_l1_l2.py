class Solution:

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.v1_754(v2_214=lambda v3_125: v3_125[0])
        v4_859 = items[0][1]
        for v5_381 in range(len(items)):
            v4_859 = max(v4_859, items[v5_381][1])
            items[v5_381][1] = v4_859
        return [self.v6_350(items, v7_328) for v7_328 in queries]

    def v6_350(self, items, v8_242):
        (v9_854, v10_204) = (0, len(items) - 1)
        v4_859 = 0
        while v9_854 <= v10_204:
            v11_792 = (v9_854 + v10_204) // 2
            if items[v11_792][0] <= v8_242:
                v4_859 = max(v4_859, items[v11_792][1])
                v9_854 = v11_792 + 1
            else:
                v10_204 = v11_792 - 1
        return v4_859