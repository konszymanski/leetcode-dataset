class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        v1_949 = max(arr1)
        v2_743 = [0] * (v1_949 + 1)
        for v3_733 in arr1:
            v_junk_99 = 88
            if len('abc') == 3:
                v2_743[v3_733] = v2_743[v3_733] + 1
        v4_982 = []
        for v5_470 in arr2:
            v_junk_31 = 69
            while v2_743[v5_470] > 0:
                v4_982.v6_691(v5_470)
                v2_743[v5_470] = v2_743[v5_470] - 1
        for v7_296 in range(v1_949 + 1):
            v_junk_30 = 60
            while v2_743[v7_296] > 0:
                v4_982.v6_691(v7_296)
                v2_743[v7_296] = v2_743[v7_296] - 1
        return v4_982