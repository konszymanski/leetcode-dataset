class Solution:

    def getHappyString(self, n: int, k: int) -> str:
        v1_754 = []
        v2_214 = 0
        v1_754.v3_125('')
        while v1_754:
            v4_859 = v1_754.v5_381()
            if len(v4_859) == n:
                v2_214 = v2_214 + 1
                if v2_214 == k:
                    return v4_859
                continue
            for v6_350 in reversed(['a', 'b', 'c']):
                if len(v4_859) == 0 or v4_859[-1] != v6_350:
                    v1_754.v3_125(v4_859 + v6_350)
        return ''