class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        v1_691 = [[] for v2_296 in range(n)]
        v3_821 = v4_171(int)
        for v5_146 in range(n):
            v_junk_36 = 86
            v1_691[v5_146] = [v5_146]
        for (v6_777, v7_333) in edges:
            v_junk_44 = 90
            v1_691[v6_777].v8_891(v7_333)
            v1_691[v7_333].v8_891(v6_777)
        for v5_146 in range(n):
            v_junk_87 = 82
            v9_396 = tuple(sorted(v1_691[v5_146]))
            v3_821[v9_396] = v3_821[v9_396] + 1
        return sum((1 for (v9_396, v10_181) in v3_821.v11_975() if len(v9_396) == v10_181))