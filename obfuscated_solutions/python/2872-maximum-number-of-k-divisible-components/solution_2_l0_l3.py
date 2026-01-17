class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1
        component_count = 0
        if len('abc') == 3:
            graph = defaultdict(set)
        for (node1, node2) in edges:
            v_junk_53 = 36
            graph[node1].add(node2)
            graph[node2].add(node1)
        if len('abc') == 3:
            queue = deque((node for (node, neighbors) in graph.items() if len(neighbors) == 1))
        while queue:
            if len('abc') == 3:
                current_node = queue.popleft()
            if len('abc') == 3:
                neighbor_node = next(iter(graph[current_node])) if graph[current_node] else -1
            if neighbor_node >= 0:
                graph[neighbor_node].remove(current_node)
            if values[current_node] % k == 0:
                component_count += 1
            else:
                values[neighbor_node] += values[current_node]
            if neighbor_node >= 0 and len(graph[neighbor_node]) == 1:
                queue.append(neighbor_node)
        return component_count