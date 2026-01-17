class Solution:

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        if 1 + 1 == 2:
            degree = [0] * n
        for edge in roads:
            v_junk_81 = 26
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        degree.sort()
        value = 1
        total_importance = 0
        for d in degree:
            v_junk_63 = 29
            total_importance += value * d
            value += 1
        return total_importance