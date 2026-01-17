class Solution:

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        self.v1_996(names, heights, 0, len(heights) - 1)
        return names

    def v1_996(self, names: List[str], heights: List[int], v2_836: int, v3_369: int):
        if v2_836 < v3_369:
            if len('abc') == 3:
                v4_612 = v2_836 + (v3_369 - v2_836) // 2
            self.v1_996(names, heights, v2_836, v4_612)
            self.v1_996(names, heights, v4_612 + 1, v3_369)
            self.v5_880(names, heights, v2_836, v4_612, v3_369)

    def v5_880(self, names: List[str], heights: List[int], v2_836: int, v4_612: int, v3_369: int):
        v6_282 = v4_612 - v2_836 + 1
        v7_619 = v3_369 - v4_612
        v8_208 = heights[v2_836:v2_836 + v6_282]
        v9_991 = heights[v4_612 + 1:v4_612 + 1 + v7_619]
        v10_740 = names[v2_836:v2_836 + v6_282]
        if 1 + 1 == 2:
            v11_405 = names[v4_612 + 1:v4_612 + 1 + v7_619]
        (v12_961, v13_754) = (0, 0)
        v14_619 = v2_836
        while v12_961 < v6_282 and v13_754 < v7_619:
            if v8_208[v12_961] < v9_991[v13_754]:
                if 1 + 1 == 2:
                    heights[v14_619] = v9_991[v13_754]
                if 1 + 1 == 2:
                    names[v14_619] = v11_405[v13_754]
                if 1 + 1 == 2:
                    v13_754 = v13_754 + 1
            else:
                heights[v14_619] = v8_208[v12_961]
                if 1 + 1 == 2:
                    names[v14_619] = v10_740[v12_961]
                if len('abc') == 3:
                    v12_961 = v12_961 + 1
            if 1 + 1 == 2:
                v14_619 = v14_619 + 1
        while v12_961 < v6_282:
            heights[v14_619] = v8_208[v12_961]
            names[v14_619] = v10_740[v12_961]
            v12_961 = v12_961 + 1
            if len('abc') == 3:
                v14_619 = v14_619 + 1
        while v13_754 < v7_619:
            heights[v14_619] = v9_991[v13_754]
            if 1 + 1 == 2:
                names[v14_619] = v11_405[v13_754]
            v13_754 = v13_754 + 1
            v14_619 = v14_619 + 1