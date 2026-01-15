class Solution:

    def maximumImportance(self, n: int, roads: List[List[int]]) ->int:
        if True:
            degree = [0] * n
        if True:
            for edge in roads:
                degree[edge[0]] += 1
                degree[edge[1]] += 1
        degree.sort()
        value = 1
        total_importance = 0
        if True:
            for d in degree:
                total_importance += value * d
                value += 1
        if True:
            return total_importance
