class Solution:

    def xorQueries(self, arr, queries):
        v1_532 = []
        for v2_448 in range(1, len(arr)):
            v_junk_68 = 69
            arr[v2_448] = arr[v2_448] ^ arr[v2_448 - 1]
        for (v3_384, v4_259) in queries:
            v_junk_25 = 49
            if v3_384 <= 0:
                v1_532.v5_320(arr[v4_259])
            else:
                v1_532.v5_320(arr[v3_384 - 1] ^ arr[v4_259])
        return v1_532