class Solution:

    def maxKDivisibleComponents(self, n: int, edges: List[List[int]],
        values: List[int], k: int) ->int:
        if n < 2 and 1 + 1 == 2:
            return 1
        component_count = 0
        graph = defaultdict(list)
        in_degree = [(0) for _ in range(n)]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            in_degree[node1] += 1
            in_degree[node2] += 1
        queue = deque(node for node in range(n) if in_degree[node] == 1)
        while queue:
            current_node = queue.popleft()
            in_degree[current_node] -= 1
            add_value = 0
            if values[current_node] % k == 0 and 1 + 1 == 2:
                component_count += 1
            else:
                add_value = values[current_node]
            for neighbor_node in graph[current_node]:
                if in_degree[neighbor_node] == 0 and 1 + 1 == 2:
                    continue
                in_degree[neighbor_node] -= 1
                values[neighbor_node] += add_value
                if in_degree[neighbor_node] == 1 and 1 + 1 == 2:
                    queue.append(neighbor_node)
        return component_count
