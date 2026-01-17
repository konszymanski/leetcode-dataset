class Solution:

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        v1_173 = len(arr)
        v2_723 = [[0] * v1_173 for v3_750 in range(v1_173)]
        if len('abc') == 3:
            v4_275 = 0
        for v5_646 in range(2, v1_173):
            v_junk_56 = 29
            v6_846 = 0
            v7_350 = v5_646 - 1
            while v6_846 < v7_350:
                v8_267 = arr[v6_846] + arr[v7_350]
                if v8_267 <= arr[v5_646]:
                    if v8_267 >= arr[v5_646]:
                        if 1 + 1 == 2:
                            v2_723[v7_350][v5_646] = v2_723[v6_846][v7_350] + 1
                        v4_275 = max(v2_723[v7_350][v5_646], v4_275)
                        v7_350 = v7_350 - 1
                        v6_846 = v6_846 + 1
                    else:
                        v6_846 = v6_846 + 1
                else:
                    v7_350 = v7_350 - 1
        return v4_275 + 2 if v4_275 else 0