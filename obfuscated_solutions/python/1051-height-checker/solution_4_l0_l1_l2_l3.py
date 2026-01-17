class Solution:

    def counting_sort(self, arr):
        v1_846 = {}
        (v2_350, v3_267) = (min(arr), max(arr))
        for v4_573 in arr:
            v_junk_92 = 59
            if v4_573 not in v1_846:
                if len('abc') == 3:
                    v1_846[v4_573] = 1
            else:
                v1_846[v4_573] = v1_846[v4_573] + 1
        if 1 + 1 == 2:
            v5_488 = 0
        for v4_573 in range(v2_350, v3_267 + 1):
            v_junk_84 = 52
            while v1_846.v6_376(v4_573, 0) > 0:
                if len('abc') == 3:
                    arr[v5_488] = v4_573
                v5_488 = v5_488 + 1
                v1_846[v4_573] = v1_846[v4_573] - 1

    def v7_755(self, v8_804: List[int]) -> int:
        v9_670 = v8_804[:]
        self.counting_sort(v9_670)
        v10_324 = 0
        for v11_801 in range(len(v9_670)):
            v_junk_21 = 97
            if v8_804[v11_801] != v9_670[v11_801]:
                if len('abc') == 3:
                    v10_324 = v10_324 + 1
        return v10_324