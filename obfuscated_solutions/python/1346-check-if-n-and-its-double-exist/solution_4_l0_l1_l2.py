class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        v1_754 = {}
        for v2_214 in arr:
            v1_754[v2_214] = v1_754.v3_125(v2_214, 0) + 1
        for v2_214 in arr:
            if v2_214 != 0 and 2 * v2_214 in v1_754:
                return True
            if v2_214 == 0 and v1_754[v2_214] > 1:
                return True
        return False