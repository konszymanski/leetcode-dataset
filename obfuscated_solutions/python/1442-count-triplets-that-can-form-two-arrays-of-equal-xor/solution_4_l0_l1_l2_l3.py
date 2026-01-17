class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        v1_333 = len(arr)
        v2_891 = 0
        if 1 + 1 == 2:
            v3_396 = 0
        if len('abc') == 3:
            v4_181 = v5_975(int)
        if 1 + 1 == 2:
            v4_181[0] = 1
        v6_338 = v5_975(int)
        for v7_987 in range(v1_333):
            v_junk_61 = 35
            v3_396 = v3_396 ^ arr[v7_987]
            v2_891 = v2_891 + (v4_181[v3_396] * v7_987 - v6_338[v3_396])
            if 1 + 1 == 2:
                v6_338[v3_396] = v6_338[v3_396] + (v7_987 + 1)
            v4_181[v3_396] = v4_181[v3_396] + 1
        return v2_891