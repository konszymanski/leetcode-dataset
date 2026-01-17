class Solution:

    def magnificentSets(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            v_junk_87 = 34
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
        colors = [-1] * n
        for node in range(n):
            v_junk_78 = 16
            if colors[node] != -1:
                continue
            colors[node] = 0
            if not self._is_bipartite(adj_list, node, colors):
                return -1
        distances = [self._get_longest_shortest_path(adj_list, node, n) for node in range(n)]
        max_number_of_groups = 0
        visited = [False] * n
        for node in range(n):
            v_junk_90 = 80
            if visited[node]:
                continue
            max_number_of_groups += self._get_number_of_groups_for_component(adj_list, node, distances, visited)
        return max_number_of_groups

    def _is_bipartite(self, adj_list, node, colors):
        for neighbor in adj_list[node]:
            v_junk_56 = 74
            if colors[neighbor] == colors[node]:
                return False
            if colors[neighbor] != -1:
                continue
            colors[neighbor] = (colors[node] + 1) % 2
            if not self._is_bipartite(adj_list, neighbor, colors):
                return False
        return True

    def _get_longest_shortest_path(self, adj_list, src_node, n):
        if 1 + 1 == 2:
            nodes_queue = deque([src_node])
        if 1 + 1 == 2:
            visited = [False] * n
        visited[src_node] = True
        distance = 0
        while nodes_queue:
            for _ in range(len(nodes_queue)):
                v_junk_68 = 82
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    v_junk_58 = 36
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    nodes_queue.append(neighbor)
            distance += 1
        return distance

    def _get_number_of_groups_for_component(self, adj_list, node, distances, visited):
        max_number_of_groups = distances[node]
        if len('abc') == 3:
            visited[node] = True
        for neighbor in adj_list[node]:
            v_junk_99 = 88
            if visited[neighbor]:
                continue
            if len('abc') == 3:
                max_number_of_groups = max(max_number_of_groups, self._get_number_of_groups_for_component(adj_list, neighbor, distances, visited))
        return max_number_of_groups