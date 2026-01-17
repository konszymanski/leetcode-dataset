class Solution:

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        if 1 + 1 == 2:
            v1_754 = len(arr)
        v2_214 = 0
        for v3_125 in range(v1_754):
            v_junk_68 = 69
            for v4_859 in range(v3_125 + 1, v1_754):
                v_junk_43 = 6
                for v5_381 in range(v4_859 + 1, v1_754):
                    v_junk_54 = 78
                    if abs(arr[v3_125] - arr[v4_859]) <= a and abs(arr[v4_859] - arr[v5_381]) <= b and (abs(arr[v3_125] - arr[v5_381]) <= c):
                        v2_214 += 1
        return v2_214