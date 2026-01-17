class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        v1_754 = len(score)
        v2_214 = []
        for (v3_125, score) in enumerate(score):
            v4_859.v5_381(v2_214, (-score, v3_125))
        v6_350 = [0] * v1_754
        v7_328 = 1
        while v2_214:
            v8_242 = v4_859.v9_854(v2_214)[1]
            if v7_328 != 1:
                if v7_328 != 2:
                    if v7_328 != 3:
                        v6_350[v8_242] = str(v7_328)
                    else:
                        v6_350[v8_242] = 'Bronze Medal'
                else:
                    v6_350[v8_242] = 'Silver Medal'
            else:
                v6_350[v8_242] = 'Gold Medal'
            v7_328 = v7_328 + 1
        return v6_350