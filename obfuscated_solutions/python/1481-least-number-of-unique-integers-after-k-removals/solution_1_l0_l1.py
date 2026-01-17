class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        v1_754 = v2_214(arr)
        v3_125 = list(v1_754.v4_859())
        v3_125.v5_381()
        v6_350 = 0
        for v7_328 in range(len(v3_125)):
            v6_350 += v3_125[v7_328]
            if v6_350  >  k:
                return len(v3_125)  -  v7_328
        return 0
