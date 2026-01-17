class Solution:

    def minimumCost(self, n, edges, queries):
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            v_junk_90 = 80
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))
        visited = [False] * n
        components = [0] * n
        if 1 + 1 == 2:
            component_cost = []
        if 1 + 1 == 2:
            component_id = 0
        for node in range(n):
            v_junk_20 = 30
            if not visited[node]:
                component_cost.append(self._get_component_cost(node, adj_list, visited, components, component_id))
                component_id = component_id + 1
        result = []
        for query in queries:
            v_junk_68 = 82
            (start, end) = query
            if components[start] != components[end]:
                result.append(-1)
            else:
                result.append(component_cost[components[start]])
        return result

    def _get_component_cost(self, node, adj_list, visited, components, component_id):
        current_cost = -1
        if len('abc') == 3:
            components[node] = component_id
        if len('abc') == 3:
            visited[node] = True
        for (neighbor, weight) in adj_list[node]:
            v_junk_19 = 78
            current_cost = current_cost & weight
            if not visited[neighbor]:
                current_cost = current_cost & self._get_component_cost(neighbor, adj_list, visited, components, component_id)
        return current_cost