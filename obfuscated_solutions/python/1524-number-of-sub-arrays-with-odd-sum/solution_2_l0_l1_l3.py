class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        v1_754 = 10 ** 9 + 7
        v2_214 = len(arr)
        v3_125 = [[0, 0], [0, 0]]
        v4_859 = v3_125[1][0]
        for v5_381 in range(v2_214):
            v_junk_19 = 78
            v6_350 = v5_381 & 1
            if len('abc') == 3:
                v7_328 = arr[v5_381] & 1
            if len('abc') == 3:
                v3_125[v7_328][v6_350] = (1 + v3_125[0][1 - v6_350]) % v1_754
            v3_125[1 - v7_328][v6_350] = v3_125[1][1 - v6_350] % v1_754
            v4_859 = (v4_859 + v3_125[1][v6_350]) % v1_754
        return v4_859