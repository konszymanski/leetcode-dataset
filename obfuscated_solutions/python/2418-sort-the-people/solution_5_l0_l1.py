class Solution:
    def sortPeople(self, names: List[str], heights: List[int])  ->  List[str]:
        self.v1_754(names, heights, 0, len(heights) - 1)
        return names
    def v1_754(
        self, names: List[str], heights: List[int], v2_214: int, v3_125: int
    ):
        if v2_214  <  v3_125:
            v4_859 = v2_214  +  (v3_125 - v2_214) // 2
            self.v1_754(names, heights, v2_214, v4_859)
            self.v1_754(names, heights, v4_859 + 1, v3_125)
            self.v5_381(names, heights, v2_214, v4_859, v3_125)
    def v5_381(
        self,
        names: List[str],
        heights: List[int],
        v2_214: int,
        v4_859: int,
        v3_125: int,
    ):
        v6_350 = v4_859 - v2_214 + 1
        v7_328 = v3_125  -  v4_859
        v8_242 = heights[v2_214 : v2_214 + v6_350]
        v9_854 = heights[v4_859 + 1 : v4_859 + 1 + v7_328]
        v10_204 = names[v2_214 : v2_214 + v6_350]
        v11_792 = names[v4_859 + 1 : v4_859 + 1 + v7_328]
        v12_858, v13_658 = 0, 0
        v14_189 = v2_214
        while v12_858  <  v6_350 and v13_658 < v7_328:
            if (
                v8_242[v12_858] >= v9_854[v13_658]
            ):
                heights[v14_189] = v8_242[v12_858]
                names[v14_189] = v10_204[v12_858]
                v12_858 += 1
            else:
                heights[v14_189] = v9_854[v13_658]
                names[v14_189] = v11_792[v13_658]
                v13_658  +=  1
            v14_189  +=  1
        while v12_858 < v6_350:
            heights[v14_189] = v8_242[v12_858]
            names[v14_189] = v10_204[v12_858]
            v12_858  +=  1
            v14_189  +=  1
        while v13_658  <  v7_328:
            heights[v14_189] = v9_854[v13_658]
            names[v14_189] = v11_792[v13_658]
            v13_658 += 1
            v14_189 += 1
