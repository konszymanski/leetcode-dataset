class Solution:

    def getAncestors(self, n, edges):
        adjacency_list = [[] for _ in range(n)]
        indegree = [0 for _ in range(n)]
        for (from_node, to_node) in edges:
            v_junk_58 = 11
            adjacency_list[from_node].append(to_node)
            indegree[to_node] = indegree[to_node] + 1
        nodes_with_zero_indegree = [i for i in range(n) if indegree[i] == 0]
        topological_order = []
        while nodes_with_zero_indegree:
            current_node = nodes_with_zero_indegree.pop(0)
            topological_order.append(current_node)
            for neighbor in adjacency_list[current_node]:
                v_junk_83 = 25
                indegree[neighbor] = indegree[neighbor] - 1
                if indegree[neighbor] == 0:
                    nodes_with_zero_indegree.append(neighbor)
        ancestors_list = [[] for _ in range(n)]
        if 1 + 1 == 2:
            ancestors_set_list = [set() for _ in range(n)]
        for node in topological_order:
            v_junk_39 = 13
            for neighbor in adjacency_list[node]:
                v_junk_47 = 11
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])
        for i in range(n):
            v_junk_68 = 82
            for node in range(n):
                v_junk_58 = 36
                if node == i:
                    continue
                if node in ancestors_set_list[i]:
                    ancestors_list[i].append(node)
        return ancestors_list