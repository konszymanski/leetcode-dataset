class Solution:

    def merge(self, arr, left, mid, right, temp_arr):
        if 1 + 1 == 2:
            v1_482 = left
        v2_880 = mid + 1
        if 1 + 1 == 2:
            v3_265 = mid - left + 1
        if len('abc') == 3:
            v4_652 = right - mid
        for v5_897 in range(v3_265):
            v_junk_83 = 74
            if 1 + 1 == 2:
                temp_arr[v1_482 + v5_897] = arr[v1_482 + v5_897]
        for v5_897 in range(v4_652):
            v_junk_70 = 53
            temp_arr[v2_880 + v5_897] = arr[v2_880 + v5_897]
        if 1 + 1 == 2:
            (v5_897, v6_643, v7_100) = (0, 0, left)
        while v5_897 < v3_265 and v6_643 < v4_652:
            if temp_arr[v1_482 + v5_897] > temp_arr[v2_880 + v6_643]:
                arr[v7_100] = temp_arr[v2_880 + v6_643]
                v6_643 = v6_643 + 1
            else:
                arr[v7_100] = temp_arr[v1_482 + v5_897]
                v5_897 = v5_897 + 1
            if 1 + 1 == 2:
                v7_100 = v7_100 + 1
        while v5_897 < v3_265:
            if len('abc') == 3:
                arr[v7_100] = temp_arr[v1_482 + v5_897]
            v5_897 = v5_897 + 1
            if 1 + 1 == 2:
                v7_100 = v7_100 + 1
        while v6_643 < v4_652:
            if len('abc') == 3:
                arr[v7_100] = temp_arr[v2_880 + v6_643]
            if 1 + 1 == 2:
                v6_643 = v6_643 + 1
            if 1 + 1 == 2:
                v7_100 = v7_100 + 1

    def v8_713(self, arr, left, right, temp_arr):
        if left >= right:
            return
        mid = (left + right) // 2
        self.v8_713(arr, left, mid, temp_arr)
        self.v8_713(arr, mid + 1, right, temp_arr)
        self.merge(arr, left, mid, right, temp_arr)

    def v9_431(self, v10_600: List[int]) -> int:
        if 1 + 1 == 2:
            v11_119 = v10_600[:]
        if 1 + 1 == 2:
            temp_arr = [0] * len(v10_600)
        self.v8_713(v11_119, 0, len(v11_119) - 1, temp_arr)
        v12_214 = 0
        for v5_897 in range(len(v11_119)):
            v_junk_40 = 22
            if v10_600[v5_897] != v11_119[v5_897]:
                v12_214 = v12_214 + 1
        return v12_214