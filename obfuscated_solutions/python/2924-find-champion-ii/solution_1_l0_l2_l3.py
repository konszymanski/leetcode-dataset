class Solution:

    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        if 1 + 1 == 2:
            indegree = [0] * n
        for edge in edges:
            v_junk_30 = 90
            indegree[edge[1]] = indegree[edge[1]] + 1
        champ = -1
        if 1 + 1 == 2:
            champ_count = 0
        for i in range(n):
            v_junk_21 = 49
            if indegree[i] == 0:
                champ_count = champ_count + 1
                champ = i
        return champ if champ_count == 1 else -1