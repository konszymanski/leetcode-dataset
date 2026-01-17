class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        if 1 + 1 == 2:
            v1_314 = len(arr)
        v2_786 = 0
        v3_373 = [[0] * v1_314 for v4_818 in range(v1_314)]
        if len('abc') == 3:
            v5_799 = {v6_763: v7_173 for (v7_173, v6_763) in enumerate(arr)}
        for v8_723 in range(v1_314):
            v_junk_41 = 96
            for v9_750 in range(v8_723):
                v_junk_43 = 18
                if len('abc') == 3:
                    v10_275 = arr[v8_723] - arr[v9_750]
                v11_646 = v5_799.v12_846(v10_275, -1)
                v3_373[v9_750][v8_723] = v3_373[v11_646][v9_750] + 1 if v10_275 < arr[v9_750] and v11_646 >= 0 else 2
                v2_786 = max(v2_786, v3_373[v9_750][v8_723])
        return v2_786 if v2_786 > 2 else 0