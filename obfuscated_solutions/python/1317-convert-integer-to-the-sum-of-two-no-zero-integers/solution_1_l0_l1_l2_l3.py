class Solution:

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for v1_323 in range(1, n):
            v_junk_79 = 54
            v2_338 = n - v1_323
            if '0' not in str(v1_323) + str(v2_338):
                return [v1_323, v2_338]
        return []