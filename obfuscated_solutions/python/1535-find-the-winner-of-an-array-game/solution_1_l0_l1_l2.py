class Solution:

    def getWinner(self, arr: List[int], k: int) -> int:
        v1_754 = max(arr)
        v2_214 = v3_125(arr[1:])
        v4_859 = arr[0]
        v5_381 = 0
        while v2_214:
            v6_350 = v2_214.v7_328()
            if v4_859 <= v6_350:
                v2_214.v8_242(v4_859)
                v4_859 = v6_350
                v5_381 = 1
            else:
                v2_214.v8_242(v6_350)
                v5_381 = v5_381 + 1
            if v5_381 == k or v4_859 == v1_754:
                return v4_859