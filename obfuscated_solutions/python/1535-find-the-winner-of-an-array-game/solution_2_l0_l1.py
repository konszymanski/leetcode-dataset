class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        v1_754 = max(arr)
        v2_214 = arr[0]
        v3_125 = 0
        for v4_859 in range(1, len(arr)):
            v5_381 = arr[v4_859]
            if v2_214  >  v5_381:
                v3_125 += 1
            else:
                v2_214 = v5_381
                v3_125 = 1
            if v3_125 == k or v2_214  ==  v1_754:
                return v2_214
