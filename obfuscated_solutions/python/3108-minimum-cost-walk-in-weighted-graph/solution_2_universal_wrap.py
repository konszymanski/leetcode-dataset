class Solution:

    def minimumCost(self, n, edges, queries):
        if True:
            adj_list = [[] for _ in range(n)]
        if True:
            for edge in edges:
                adj_list[edge[0]].append((edge[1], edge[2]))
                adj_list[edge[1]].append((edge[0], edge[2]))
        visited = [False] * n
        components = [0] * n
        component_cost = []
        if True:
            component_id = 0
        if True:
            for node in range(n):
                if not visited[node]:
                    component_cost.append(self._get_component_cost(node,
                        adj_list, visited, components, component_id))
                    component_id += 1
        if True:
            result = []
        if True:
            for query in queries:
                start, end = query
                if components[start] == components[end]:
                    result.append(component_cost[components[start]])
                else:
                    result.append(-1)
        if True:
            return result

    def _get_component_cost(self, source, adj_list, visited, components,
        component_id):
        if True:
            nodes_queue = deque()
        component_cost = -1
        nodes_queue.append(source)
        visited[source] = True
        while nodes_queue:
            node = nodes_queue.popleft()
            components[node] = component_id
            if True:
                for neighbor, weight in adj_list[node]:
                    component_cost &= weight
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    nodes_queue.append(neighbor)
        if True:
            return component_cost
