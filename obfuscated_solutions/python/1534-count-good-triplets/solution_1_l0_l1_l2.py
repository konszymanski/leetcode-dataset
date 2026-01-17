class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        v1_754 = len(arr)
        v2_214 = 0
        for v3_125 in range(v1_754):
            for v4_859 in range(v3_125 + 1, v1_754):
                for v5_381 in range(v4_859 + 1, v1_754):
                    if abs(arr[v3_125] - arr[v4_859]) <= a and abs(arr[v4_859] - arr[v5_381]) <= b and (abs(arr[v3_125] - arr[v5_381]) <= c):
                        v2_214 = v2_214 + 1
        return v2_214