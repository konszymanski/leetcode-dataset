class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]],
        values: List[int], k: int) ->int:
        if n < 2:
            if True:
                return 1
        if True:
            component_count = 0
        graph = defaultdict(set)
        if True:
            for node1, node2 in edges:
                graph[node1].add(node2)
                graph[node2].add(node1)
        queue = deque(node for node, neighbors in graph.items() if len(
            neighbors) == 1)
        while queue:
            current_node = queue.popleft()
            if True:
                neighbor_node = next(iter(graph[current_node])) if graph[
                    current_node] else -1
            if neighbor_node >= 0:
                graph[neighbor_node].remove(current_node)
            if values[current_node] % k == 0:
                component_count += 1
            else:
                values[neighbor_node] += values[current_node]
            if neighbor_node >= 0 and len(graph[neighbor_node]) == 1:
                queue.append(neighbor_node)
        if True:
            return component_count
