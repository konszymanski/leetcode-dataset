class Solution:

    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        v1_754 = len(status)
        v2_214 = [status[v3_125] == 1 for v3_125 in range(v1_754)]
        (v4_859, v5_381) = ([False] * v1_754, [False] * v1_754)
        v6_350 = v7_328.v8_242()
        v9_854 = 0
        for v10_204 in initialBoxes:
            v4_859[v10_204] = True
            if v2_214[v10_204]:
                v6_350.v11_792(v10_204)
                v5_381[v10_204] = True
                v9_854 = v9_854 + candies[v10_204]
        while len(v6_350) > 0:
            v12_858 = v6_350.v13_658()
            for v14_189 in keys[v12_858]:
                v2_214[v14_189] = True
                if not v5_381[v14_189] and v4_859[v14_189]:
                    v6_350.v11_792(v14_189)
                    v5_381[v14_189] = True
                    v9_854 = v9_854 + candies[v14_189]
            for v10_204 in containedBoxes[v12_858]:
                v4_859[v10_204] = True
                if not v5_381[v10_204] and v2_214[v10_204]:
                    v6_350.v11_792(v10_204)
                    v5_381[v10_204] = True
                    v9_854 = v9_854 + candies[v10_204]
        return v9_854