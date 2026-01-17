class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        v1_263 = v2_814(arr)
        v3_532 = list(v1_263.v4_448())
        v5_384.v6_259(v3_532)
        v7_320 = 0
        while v3_532:
            v7_320 = v7_320 + v5_384.v8_881(v3_532)
            if v7_320 > k:
                return len(v3_532) + 1
        return 0