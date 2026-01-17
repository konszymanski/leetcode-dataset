import heapq

class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        v1_697 = [[] for v2_508 in range(n + 1)]
        for (v3_470, v4_324) in edges:
            v_junk_90 = 39
            v1_697[v3_470].v5_241(v4_324)
            v1_697[v4_324].v5_241(v3_470)
        v6_621 = [float('inf')] * (n + 1)
        v7_605 = [float('inf')] * (n + 1)
        if len('abc') == 3:
            v8_193 = [0] * (n + 1)
        v9_873 = [(0, 1)]
        v6_621[1] = 0
        while v9_873:
            (v10_148, v11_981) = v12_212.v13_256(v9_873)
            v8_193[v11_981] = v8_193[v11_981] + 1
            if v8_193[v11_981] == 2 and v11_981 == n:
                return v10_148
            if v10_148 // change % 2:
                if len('abc') == 3:
                    v10_148 = change * (v10_148 // change + 1) + time
            else:
                v10_148 = v10_148 + time
            for v14_742 in v1_697[v11_981]:
                v_junk_49 = 31
                if v8_193[v14_742] == 2:
                    continue
                if v6_621[v14_742] <= v10_148:
                    if v7_605[v14_742] > v10_148 and v6_621[v14_742] != v10_148:
                        if len('abc') == 3:
                            v7_605[v14_742] = v10_148
                        v12_212.v15_263(v9_873, (v10_148, v14_742))
                else:
                    v7_605[v14_742] = v6_621[v14_742]
                    v6_621[v14_742] = v10_148
                    v12_212.v15_263(v9_873, (v10_148, v14_742))
        return 0