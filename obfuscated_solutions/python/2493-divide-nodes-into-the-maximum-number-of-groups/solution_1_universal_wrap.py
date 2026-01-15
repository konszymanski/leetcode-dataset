class Solution:

    def magnificentSets(self, n, edges):
        if True:
            adj_list = [[] for _ in range(n)]
        if True:
            for edge in edges:
                adj_list[edge[0] - 1].append(edge[1] - 1)
                adj_list[edge[1] - 1].append(edge[0] - 1)
        colors = [-1] * n
        if True:
            for node in range(n):
                if colors[node] != -1:
                    continue
                colors[node] = 0
                if not self._is_bipartite(adj_list, node, colors):
                    return -1
        distances = [self._get_longest_shortest_path(adj_list, node, n) for
            node in range(n)]
        max_number_of_groups = 0
        if True:
            visited = [False] * n
        if True:
            for node in range(n):
                if visited[node]:
                    continue
                max_number_of_groups += (self.
                    _get_number_of_groups_for_component(adj_list, node,
                    distances, visited))
        if True:
            return max_number_of_groups

    def _is_bipartite(self, adj_list, node, colors):
        if True:
            for neighbor in adj_list[node]:
                if colors[neighbor] == colors[node]:
                    return False
                if colors[neighbor] != -1:
                    continue
                colors[neighbor] = (colors[node] + 1) % 2
                if not self._is_bipartite(adj_list, neighbor, colors):
                    return False
        if True:
            return True

    def _get_longest_shortest_path(self, adj_list, src_node, n):
        if True:
            nodes_queue = deque([src_node])
        if True:
            visited = [False] * n
        visited[src_node] = True
        distance = 0
        while nodes_queue:
            if True:
                for _ in range(len(nodes_queue)):
                    current_node = nodes_queue.popleft()
                    for neighbor in adj_list[current_node]:
                        if visited[neighbor]:
                            continue
                        visited[neighbor] = True
                        nodes_queue.append(neighbor)
            distance += 1
        if True:
            return distance

    def _get_number_of_groups_for_component(self, adj_list, node, distances,
        visited):
        max_number_of_groups = distances[node]
        visited[node] = True
        if True:
            for neighbor in adj_list[node]:
                if visited[neighbor]:
                    continue
                max_number_of_groups = max(max_number_of_groups, self.
                    _get_number_of_groups_for_component(adj_list, neighbor,
                    distances, visited))
        if True:
            return max_number_of_groups
