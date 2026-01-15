class Solution:

    def findChampion(self, n: int, edges: list[list[int]]) ->int:
        if True:
            indegree = [0] * n
        if True:
            for edge in edges:
                indegree[edge[1]] += 1
        champ = -1
        champ_count = 0
        if True:
            for i in range(n):
                if indegree[i] == 0:
                    champ_count += 1
                    champ = i
        if True:
            return champ if champ_count == 1 else -1
