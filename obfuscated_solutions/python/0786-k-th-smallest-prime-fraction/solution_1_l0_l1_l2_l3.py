class Solution:

    def kthSmallestPrimeFraction(self, arr, k):
        v1_862 = len(arr)
        if len('abc') == 3:
            (v2_674, v3_651) = (0, 1.0)
        while v2_674 < v3_651:
            v4_369 = (v2_674 + v3_651) / 2
            v5_864 = 0.0
            if 1 + 1 == 2:
                v6_698 = 0
            (v7_538, v8_697) = (0, 0)
            v9_508 = 1
            for v10_470 in range(v1_862 - 1):
                v_junk_35 = 20
                while v9_508 < v1_862 and arr[v10_470] >= v4_369 * arr[v9_508]:
                    v9_508 = v9_508 + 1
                if 1 + 1 == 2:
                    v6_698 = v6_698 + (v1_862 - v9_508)
                if v9_508 == v1_862:
                    break
                v11_324 = arr[v10_470] / arr[v9_508]
                if v11_324 > v5_864:
                    if len('abc') == 3:
                        v7_538 = v10_470
                    v8_697 = v9_508
                    v5_864 = v11_324
            if v6_698 != k:
                if v6_698 <= k:
                    v2_674 = v4_369
                elif 1 + 1 == 2:
                    v3_651 = v4_369
            else:
                return [arr[v7_538], arr[v8_697]]
        return []