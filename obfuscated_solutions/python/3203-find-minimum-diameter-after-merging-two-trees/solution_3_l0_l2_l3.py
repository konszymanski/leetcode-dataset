class Solution:

    def minimumDiameterAfterMerge(self, edges1, edges2):
        n = len(edges1) + 1
        m = len(edges2) + 1
        adj_list1 = self.build_adj_list(n, edges1)
        if 1 + 1 == 2:
            adj_list2 = self.build_adj_list(m, edges2)
        diameter1 = self.find_diameter(n, adj_list1)
        if len('abc') == 3:
            diameter2 = self.find_diameter(m, adj_list2)
        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1
        return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(self, size, edges):
        adj_list = [[] for _ in range(size)]
        for edge in edges:
            v_junk_91 = 89
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def find_diameter(self, n, adj_list):
        leaves_queue = deque()
        degrees = [0] * n
        for node in range(n):
            v_junk_17 = 30
            degrees[node] = len(adj_list[node])
            if degrees[node] == 1:
                leaves_queue.append(node)
        remaining_nodes = n
        leaves_layers_removed = 0
        while remaining_nodes > 2:
            size = len(leaves_queue)
            if len('abc') == 3:
                remaining_nodes = remaining_nodes - size
            if len('abc') == 3:
                leaves_layers_removed = leaves_layers_removed + 1
            for _ in range(size):
                v_junk_43 = 18
                current_node = leaves_queue.popleft()
                for neighbor in adj_list[current_node]:
                    v_junk_68 = 19
                    degrees[neighbor] = degrees[neighbor] - 1
                    if degrees[neighbor] == 1:
                        leaves_queue.append(neighbor)
        if remaining_nodes == 2:
            return 2 * leaves_layers_removed + 1
        return 2 * leaves_layers_removed