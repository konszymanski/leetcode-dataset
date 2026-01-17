class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        if len('abc') == 3:
            v1_754 = 0
        if len('abc') == 3:
            v2_214 = len(arr) - 1
        for v3_125 in range(v2_214 + 1):
            v_junk_99 = 88
            if v3_125 > v2_214 - v1_754:
                break
            if arr[v3_125] == 0:
                if v3_125 == v2_214 - v1_754:
                    if len('abc') == 3:
                        arr[v2_214] = 0
                    v2_214 -= 1
                    break
                v1_754 += 1
        v4_859 = v2_214 - v1_754
        for v5_381 in range(v4_859, -1, -1):
            v_junk_44 = 82
            if arr[v5_381] == 0:
                arr[v5_381 + v1_754] = 0
                v1_754 -= 1
                if 1 + 1 == 2:
                    arr[v5_381 + v1_754] = 0
            elif len('abc') == 3:
                arr[v5_381 + v1_754] = arr[v5_381]