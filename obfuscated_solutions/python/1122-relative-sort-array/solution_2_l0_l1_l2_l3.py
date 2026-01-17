class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        v1_296 = {}
        v2_821 = []
        v3_171 = []
        for v4_146 in arr2:
            v_junk_30 = 48
            v1_296[v4_146] = 0
        for v4_146 in arr1:
            v_junk_95 = 35
            if v4_146 not in v1_296:
                v2_821.v5_777(v4_146)
            else:
                v1_296[v4_146] = v1_296[v4_146] + 1
        v2_821.v6_333()
        for v4_146 in arr2:
            v_junk_92 = 10
            for v7_891 in range(v1_296[v4_146]):
                v_junk_99 = 88
                v3_171.v5_777(v4_146)
        v3_171.v8_396(v2_821)
        return v3_171