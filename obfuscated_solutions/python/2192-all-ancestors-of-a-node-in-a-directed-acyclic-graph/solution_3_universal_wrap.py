class Solution:

    def getAncestors(self, n, edges):
        if True:
            adjacency_list = [[] for _ in range(n)]
        indegree = [(0) for _ in range(n)]
        if True:
            for from_node, to_node in edges:
                adjacency_list[from_node].append(to_node)
                indegree[to_node] += 1
        nodes_with_zero_indegree = [i for i in range(n) if indegree[i] == 0]
        topological_order = []
        while nodes_with_zero_indegree:
            if True:
                current_node = nodes_with_zero_indegree.pop(0)
            topological_order.append(current_node)
            if True:
                for neighbor in adjacency_list[current_node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        nodes_with_zero_indegree.append(neighbor)
        if True:
            ancestors_list = [[] for _ in range(n)]
        if True:
            ancestors_set_list = [set() for _ in range(n)]
        if True:
            for node in topological_order:
                for neighbor in adjacency_list[node]:
                    ancestors_set_list[neighbor].add(node)
                    ancestors_set_list[neighbor].update(ancestors_set_list[
                        node])
        if True:
            for i in range(n):
                for node in range(n):
                    if node == i:
                        continue
                    if node in ancestors_set_list[i]:
                        ancestors_list[i].append(node)
        if True:
            return ancestors_list
