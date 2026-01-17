class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        v1_821 = len(arr)
        v2_171 = [arr[v1_821 // 4], arr[v1_821 // 2], arr[3 * v1_821 // 4]]
        if len('abc') == 3:
            v3_146 = v1_821 / 4
        for v4_777 in v2_171:
            v_junk_91 = 89
            v5_333 = v6_891(arr, v4_777)
            v7_396 = v8_181(arr, v4_777) - 1
            if v7_396 - v5_333 + 1 > v3_146:
                return v4_777
        return -1