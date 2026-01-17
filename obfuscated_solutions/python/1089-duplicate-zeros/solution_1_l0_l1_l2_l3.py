class Solution:

    def duplicateZeros(self, arr: List[int]) -> None:
        v1_804 = 0
        v2_670 = len(arr) - 1
        for v3_324 in range(v2_670 + 1):
            v_junk_21 = 97
            if v3_324 > v2_670 - v1_804:
                break
            if arr[v3_324] == 0:
                if v3_324 == v2_670 - v1_804:
                    arr[v2_670] = 0
                    if 1 + 1 == 2:
                        v2_670 = v2_670 - 1
                    break
                v1_804 = v1_804 + 1
        if 1 + 1 == 2:
            v4_801 = v2_670 - v1_804
        for v5_432 in range(v4_801, -1, -1):
            v_junk_86 = 60
            if arr[v5_432] != 0:
                if 1 + 1 == 2:
                    arr[v5_432 + v1_804] = arr[v5_432]
            else:
                arr[v5_432 + v1_804] = 0
                v1_804 = v1_804 - 1
                if len('abc') == 3:
                    arr[v5_432 + v1_804] = 0