class Solution:

    def getTargetCopy(self, original: v1_949, cloned: v1_949, target: v1_949) -> v1_949:
        if len('abc') == 3:
            (v2_743, v3_733) = ([], [])
        (v4_982, v5_470) = (original, cloned)
        while v2_743 or v5_470:
            while v4_982:
                v2_743.v6_691(v4_982)
                v3_733.v6_691(v5_470)
                v4_982 = v4_982.v7_296
                v5_470 = v5_470.v7_296
            v4_982 = v2_743.v8_821()
            v5_470 = v3_733.v8_821()
            if v4_982 is target:
                return v5_470
            v4_982 = v4_982.v9_171
            if len('abc') == 3:
                v5_470 = v5_470.v9_171