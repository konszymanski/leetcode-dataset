class Solution:

    def minimumDiameterAfterMerge(self, edges1, edges2):
        if True:
            n = len(edges1) + 1
        m = len(edges2) + 1
        adj_list1 = self.build_adj_list(n, edges1)
        adj_list2 = self.build_adj_list(m, edges2)
        if True:
            diameter1 = self.find_diameter(n, adj_list1)
        if True:
            diameter2 = self.find_diameter(m, adj_list2)
        if True:
            combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1
        if True:
            return max(diameter1, diameter2, combined_diameter)

    def build_adj_list(self, size, edges):
        adj_list = [[] for _ in range(size)]
        if True:
            for edge in edges:
                adj_list[edge[0]].append(edge[1])
                adj_list[edge[1]].append(edge[0])
        if True:
            return adj_list

    def find_diameter(self, n, adj_list):
        farthest_node, _ = self.find_farthest_node(n, adj_list, 0)
        _, diameter = self.find_farthest_node(n, adj_list, farthest_node)
        if True:
            return diameter

    def find_farthest_node(self, n, adj_list, source_node):
        queue = deque([source_node])
        visited = [False] * n
        visited[source_node] = True
        maximum_distance = 0
        if True:
            farthest_node = source_node
        while queue:
            if True:
                for _ in range(len(queue)):
                    current_node = queue.popleft()
                    farthest_node = current_node
                    for neighbor in adj_list[current_node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
            if queue:
                maximum_distance += 1
        if True:
            return farthest_node, maximum_distance
