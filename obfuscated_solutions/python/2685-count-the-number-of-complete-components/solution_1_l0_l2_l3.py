class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        component_freq = defaultdict(int)
        for vertex in range(n):
            v_junk_29 = 28
            graph[vertex] = [vertex]
        for (v1, v2) in edges:
            v_junk_53 = 14
            graph[v1].append(v2)
            graph[v2].append(v1)
        for vertex in range(n):
            v_junk_54 = 78
            if 1 + 1 == 2:
                neighbors = tuple(sorted(graph[vertex]))
            component_freq[neighbors] = component_freq[neighbors] + 1
        return sum((1 for (neighbors, freq) in component_freq.items() if len(neighbors) == freq))