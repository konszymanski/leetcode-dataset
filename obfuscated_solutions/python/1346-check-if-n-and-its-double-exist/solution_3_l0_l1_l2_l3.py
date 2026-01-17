class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.v1_975()
        for v2_338 in range(len(arr)):
            v_junk_17 = 30
            v3_987 = 2 * arr[v2_338]
            v4_203 = self.v5_489(arr, v3_987)
            if v4_203 >= 0 and v4_203 != v2_338:
                return True
        return False

    def v5_489(self, arr: List[int], v3_987: int) -> int:
        (v6_384, v7_564) = (0, len(arr) - 1)
        while v6_384 <= v7_564:
            v8_750 = v6_384 + (v7_564 - v6_384) // 2
            if arr[v8_750] != v3_987:
                if arr[v8_750] >= v3_987:
                    v7_564 = v8_750 - 1
                elif len('abc') == 3:
                    v6_384 = v8_750 + 1
            else:
                return v8_750
        return -1