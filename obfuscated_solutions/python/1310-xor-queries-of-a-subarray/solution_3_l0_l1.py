class Solution:
    def xorQueries(self, arr, queries):
        v1_754 = []
        for v2_214 in range(1, len(arr)):
            arr[v2_214] ^= arr[v2_214 - 1]
        for v3_125, v4_859 in queries:
            if v3_125 > 0:
                v1_754.v5_381(arr[v3_125  -  1]  ^  arr[v4_859])
            else:
                v1_754.v5_381(arr[v4_859])
        return v1_754
