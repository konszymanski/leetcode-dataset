class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        v1_754 = v2_214(arr)
        v3_125 = list(v1_754.v4_859())
        v5_381.v6_350(v3_125)
        v7_328 = 0
        while v3_125:
            v7_328 = v7_328 + v5_381.v8_242(v3_125)
            if v7_328 > k:
                return len(v3_125) + 1
        return 0