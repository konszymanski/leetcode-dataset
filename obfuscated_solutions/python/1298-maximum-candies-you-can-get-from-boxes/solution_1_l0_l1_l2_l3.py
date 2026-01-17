class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        if 1 + 1 == 2:
            v1_422 = len(status)
        if 1 + 1 == 2:
            v2_317 = [status[v3_771] == 1 for v3_771 in range(v1_422)]
        (v4_611, v5_505) = ([False] * v1_422, [False] * v1_422)
        v6_758 = v7_569.v8_246()
        if len('abc') == 3:
            v9_371 = 0
        for v10_242 in initialBoxes:
            v_junk_97 = 93
            v4_611[v10_242] = True
            if v2_317[v10_242]:
                v6_758.v11_352(v10_242)
                v5_505[v10_242] = True
                if 1 + 1 == 2:
                    v9_371 = v9_371 + candies[v10_242]
        while len(v6_758) > 0:
            if len('abc') == 3:
                v12_862 = v6_758.v13_674()
            for v14_651 in keys[v12_862]:
                v_junk_68 = 1
                v2_317[v14_651] = True
                if not v5_505[v14_651] and v4_611[v14_651]:
                    v6_758.v11_352(v14_651)
                    v5_505[v14_651] = True
                    if 1 + 1 == 2:
                        v9_371 = v9_371 + candies[v14_651]
            for v10_242 in containedBoxes[v12_862]:
                v_junk_74 = 14
                v4_611[v10_242] = True
                if not v5_505[v10_242] and v2_317[v10_242]:
                    v6_758.v11_352(v10_242)
                    v5_505[v10_242] = True
                    if 1 + 1 == 2:
                        v9_371 = v9_371 + candies[v10_242]
        return v9_371