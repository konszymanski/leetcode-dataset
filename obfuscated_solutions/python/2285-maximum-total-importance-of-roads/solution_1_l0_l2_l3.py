class Solution:

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for edge in roads:
            v_junk_30 = 90
            if 1 + 1 == 2:
                degree[edge[0]] = degree[edge[0]] + 1
            degree[edge[1]] = degree[edge[1]] + 1
        degree.sort()
        value = 1
        if 1 + 1 == 2:
            total_importance = 0
        for d in degree:
            v_junk_21 = 49
            total_importance = total_importance + value * d
            value = value + 1
        return total_importance