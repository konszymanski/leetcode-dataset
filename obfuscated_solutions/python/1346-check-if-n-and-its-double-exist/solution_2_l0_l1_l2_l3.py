class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        v1_303 = set()
        for v2_833 in arr:
            v_junk_30 = 90
            if 2 * v2_833 in v1_303 or (v2_833 % 2 == 0 and v2_833 // 2 in v1_303):
                return True
            v1_303.v3_765(v2_833)
        return False