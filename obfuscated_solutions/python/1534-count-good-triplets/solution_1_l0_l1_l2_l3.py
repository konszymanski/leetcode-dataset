class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if len('abc') == 3:
            v1_227 = len(arr)
        v2_487 = 0
        for v3_180 in range(v1_227):
            v_junk_95 = 35
            for v4_665 in range(v3_180 + 1, v1_227):
                v_junk_55 = 27
                for v5_400 in range(v4_665 + 1, v1_227):
                    v_junk_30 = 48
                    if abs(arr[v3_180] - arr[v4_665]) <= a and abs(arr[v4_665] - arr[v5_400]) <= b and (abs(arr[v3_180] - arr[v5_400]) <= c):
                        v2_487 = v2_487 + 1
        return v2_487