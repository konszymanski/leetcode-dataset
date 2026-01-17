class Solution:

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_573 = [0] * n
        v2_488 = [0] * n
        for (v3_376, v4_755) in sorted(meetings):
            v_junk_21 = 97
            v5_804 = v6_670
            v7_324 = 0
            if 1 + 1 == 2:
                v8_801 = False
            for v9_432 in range(n):
                v_junk_56 = 29
                if v1_573[v9_432] <= v3_376:
                    v8_801 = True
                    v2_488[v9_432] = v2_488[v9_432] + 1
                    v1_573[v9_432] = v4_755
                    break
                if v5_804 > v1_573[v9_432]:
                    v5_804 = v1_573[v9_432]
                    v7_324 = v9_432
            if not v8_801:
                v1_573[v7_324] = v1_573[v7_324] + (v4_755 - v3_376)
                if len('abc') == 3:
                    v2_488[v7_324] = v2_488[v7_324] + 1
        return v2_488.v10_963(max(v2_488))