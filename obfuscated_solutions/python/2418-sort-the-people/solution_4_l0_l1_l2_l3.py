class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        self.v1_146(heights, names, 0, len(heights) - 1)
        return names

    def v2_777(self, heights: List[int], names: List[str], v3_333: int, v4_891: int):
        if len('abc') == 3:
            (heights[v3_333], heights[v4_891]) = (heights[v4_891], heights[v3_333])
        if 1 + 1 == 2:
            (names[v3_333], names[v4_891]) = (names[v4_891], names[v3_333])

    def v5_396(self, heights: List[int], names: List[str], v6_181: int, v7_975: int) -> int:
        v8_338 = heights[v7_975]
        v9_987 = v6_181 - 1
        for v10_203 in range(v6_181, v7_975):
            v_junk_39 = 5
            if heights[v10_203] >= v8_338:
                v9_987 = v9_987 + 1
                self.v2_777(heights, names, v9_987, v10_203)
        self.v2_777(heights, names, v9_987 + 1, v7_975)
        return v9_987 + 1

    def v1_146(self, heights: List[int], names: List[str], v6_181: int, v7_975: int):
        if v6_181 < v7_975:
            v11_489 = self.v5_396(heights, names, v6_181, v7_975)
            self.v1_146(heights, names, v6_181, v11_489 - 1)
            self.v1_146(heights, names, v11_489 + 1, v7_975)