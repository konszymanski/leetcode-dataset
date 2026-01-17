class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        arr.v1_754()
        for v2_214 in range(len(arr)):
            v3_125 = 2 * arr[v2_214]
            v4_859 = self.v5_381(arr, v3_125)
            if v4_859 >= 0 and v4_859 != v2_214:
                return True
        return False

    def v5_381(self, arr: List[int], v3_125: int) -> int:
        (v6_350, v7_328) = (0, len(arr) - 1)
        while v6_350 <= v7_328:
            v8_242 = v6_350 + (v7_328 - v6_350) // 2
            if arr[v8_242] != v3_125:
                if arr[v8_242] >= v3_125:
                    v7_328 = v8_242 - 1
                else:
                    v6_350 = v8_242 + 1
            else:
                return v8_242
        return -1