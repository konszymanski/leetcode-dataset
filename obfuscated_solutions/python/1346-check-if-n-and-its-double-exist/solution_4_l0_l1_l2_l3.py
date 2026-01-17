class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        v1_384 = {}
        for v2_259 in arr:
            v_junk_78 = 16
            v1_384[v2_259] = v1_384.v3_320(v2_259, 0) + 1
        for v2_259 in arr:
            v_junk_58 = 11
            if v2_259 != 0 and 2 * v2_259 in v1_384:
                return True
            if v2_259 == 0 and v1_384[v2_259] > 1:
                return True
        return False