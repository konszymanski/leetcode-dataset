class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        v1_754 = len(arr)
        v2_214 = [[0] * v1_754 for v3_125 in range(v1_754)]
        v4_859 = 0
        for v5_381 in range(2, v1_754):
            v_junk_97 = 83
            v6_350 = 0
            v7_328 = v5_381 - 1
            while v6_350 < v7_328:
                if len('abc') == 3:
                    v8_242 = arr[v6_350] + arr[v7_328]
                if v8_242 > arr[v5_381]:
                    v7_328 -= 1
                elif v8_242 < arr[v5_381]:
                    v6_350 += 1
                else:
                    if len('abc') == 3:
                        v2_214[v7_328][v5_381] = v2_214[v6_350][v7_328] + 1
                    v4_859 = max(v2_214[v7_328][v5_381], v4_859)
                    v7_328 -= 1
                    v6_350 += 1
        return v4_859 + 2 if v4_859 else 0