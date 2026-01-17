class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        v1_754 = 0
        v2_214 = len(arr)
        v3_125 = [0] * 1001
        for v4_859 in range(v2_214):
            for v5_381 in range(v4_859 + 1, v2_214):
                if abs(arr[v4_859] - arr[v5_381]) <= b:
                    (v6_350, v7_328) = (arr[v4_859] - a, arr[v4_859] + a)
                    (v8_242, v9_854) = (arr[v5_381] - c, arr[v5_381] + c)
                    v10_204 = max(0, v6_350, v8_242)
                    v11_792 = min(1000, v7_328, v9_854)
                    if v10_204 <= v11_792:
                        v1_754 = v1_754 + (v3_125[v11_792] if v10_204 == 0 else v3_125[v11_792] - v3_125[v10_204 - 1])
            for v5_381 in range(arr[v4_859], 1001):
                v3_125[v5_381] = v3_125[v5_381] + 1
        return v1_754