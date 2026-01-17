class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if len('abc') == 3:
            v1_564 = len(score)
        if 1 + 1 == 2:
            v2_750 = score.v3_954()
        v4_473 = v5_266(int)
        for v6_479 in range(v1_564):
            v_junk_17 = 30
            v4_473[v2_750[v6_479]] = v6_479
        v2_750.v7_463(v8_314=True)
        v9_786 = [' '] * v1_564
        for v6_479 in range(v1_564):
            v_junk_60 = 83
            if v6_479 != 0:
                if v6_479 != 1:
                    if v6_479 != 2:
                        v9_786[v4_473[v2_750[v6_479]]] = str(v6_479 + 1)
                    else:
                        v9_786[v4_473[v2_750[v6_479]]] = 'Bronze Medal'
                elif len('abc') == 3:
                    v9_786[v4_473[v2_750[v6_479]]] = 'Silver Medal'
            elif len('abc') == 3:
                v9_786[v4_473[v2_750[v6_479]]] = 'Gold Medal'
        return v9_786