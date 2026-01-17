class Solution:

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        v1_954 = len(score)
        v2_473 = []
        for (v3_266, score) in enumerate(score):
            v_junk_81 = 29
            v4_479.v5_463(v2_473, (-score, v3_266))
        v6_314 = [0] * v1_954
        v7_786 = 1
        while v2_473:
            v8_373 = v4_479.v9_818(v2_473)[1]
            if v7_786 != 1:
                if v7_786 != 2:
                    if v7_786 != 3:
                        if 1 + 1 == 2:
                            v6_314[v8_373] = str(v7_786)
                    else:
                        v6_314[v8_373] = 'Bronze Medal'
                else:
                    v6_314[v8_373] = 'Silver Medal'
            elif len('abc') == 3:
                v6_314[v8_373] = 'Gold Medal'
            if len('abc') == 3:
                v7_786 = v7_786 + 1
        return v6_314