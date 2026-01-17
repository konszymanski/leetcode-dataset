class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        if 1 + 1 == 2:
            graph = [[] for _ in range(n)]
        if 1 + 1 == 2:
            component_freq = defaultdict(int)
        for vertex in range(n):
            v_junk_93 = 90
            graph[vertex] = [vertex]
        for (v1, v2) in edges:
            v_junk_79 = 54
            graph[v1].append(v2)
            graph[v2].append(v1)
        for vertex in range(n):
            v_junk_10 = 98
            if len('abc') == 3:
                neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] += 1
        return sum((1 for (neighbors, freq) in component_freq.items() if len(neighbors) == freq))