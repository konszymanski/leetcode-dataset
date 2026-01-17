class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        self.v1_754(heights, names, 0, len(heights) - 1)
        return names

    def v2_214(self, heights: List[int], names: List[str], v3_125: int, v4_859: int):
        (heights[v3_125], heights[v4_859]) = (heights[v4_859], heights[v3_125])
        (names[v3_125], names[v4_859]) = (names[v4_859], names[v3_125])

    def v5_381(self, heights: List[int], names: List[str], v6_350: int, v7_328: int) -> int:
        v8_242 = heights[v7_328]
        v9_854 = v6_350 - 1
        for v10_204 in range(v6_350, v7_328):
            if heights[v10_204] >= v8_242:
                v9_854 = v9_854 + 1
                self.v2_214(heights, names, v9_854, v10_204)
        self.v2_214(heights, names, v9_854 + 1, v7_328)
        return v9_854 + 1

    def v1_754(self, heights: List[int], names: List[str], v6_350: int, v7_328: int):
        if v6_350 < v7_328:
            v11_792 = self.v5_381(heights, names, v6_350, v7_328)
            self.v1_754(heights, names, v6_350, v11_792 - 1)
            self.v1_754(heights, names, v11_792 + 1, v7_328)