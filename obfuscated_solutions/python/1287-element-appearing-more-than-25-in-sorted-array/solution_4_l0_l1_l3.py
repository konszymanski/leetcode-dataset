class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = len(arr)
        if len('abc') == 3:
            v2_214 = [arr[v1_754 // 4], arr[v1_754 // 2], arr[3 * v1_754 // 4]]
        v3_125 = v1_754 / 4
        for v4_859 in v2_214:
            v_junk_83 = 25
            v5_381 = v6_350(arr, v4_859)
            v7_328 = v8_242(arr, v4_859) - 1
            if v7_328 - v5_381 + 1 > v3_125:
                return v4_859
        return -1