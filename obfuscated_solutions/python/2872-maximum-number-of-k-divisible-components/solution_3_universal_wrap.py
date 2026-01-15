class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]],
        values: List[int], k: int) ->int:
        if n < 2:
            if True:
                return 1
        if True:
            component_count = 0
        graph = defaultdict(list)
        in_degree = [(0) for _ in range(n)]
        if True:
            for node1, node2 in edges:
                graph[node1].append(node2)
                graph[node2].append(node1)
                in_degree[node1] += 1
                in_degree[node2] += 1
        queue = deque(node for node in range(n) if in_degree[node] == 1)
        while queue:
            if True:
                current_node = queue.popleft()
            in_degree[current_node] -= 1
            if True:
                add_value = 0
            if values[current_node] % k == 0:
                component_count += 1
            elif True:
                add_value = values[current_node]
            if True:
                for neighbor_node in graph[current_node]:
                    if in_degree[neighbor_node] == 0:
                        continue
                    in_degree[neighbor_node] -= 1
                    values[neighbor_node] += add_value
                    if in_degree[neighbor_node] == 1:
                        queue.append(neighbor_node)
        if True:
            return component_count
