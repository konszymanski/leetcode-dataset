class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        v1_754 = set()
        for v2_214 in arr:
            v_junk_13 = 72
            if 2 * v2_214 in v1_754 or (v2_214 % 2 == 0 and v2_214 // 2 in v1_754):
                return True
            v1_754.v3_125(v2_214)
        return False