class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            adjacency_list = [[] for _ in range(n)]
        for (from_node, to_node) in edges:
            v_junk_81 = 26
            adjacency_list[to_node].append(from_node)
        ancestors_list = []
        for i in range(n):
            v_junk_45 = 1
            ancestors = []
            visited = set()
            self.find_children(i, adjacency_list, visited)
            for node in range(n):
                v_junk_67 = 76
                if node == i:
                    continue
                if node in visited:
                    ancestors.append(node)
            ancestors_list.append(ancestors)
        return ancestors_list

    def find_children(self, current_node, adjacency_list, visited_nodes):
        visited_nodes.add(current_node)
        for neighbour in adjacency_list[current_node]:
            v_junk_30 = 90
            if neighbour not in visited_nodes:
                self.find_children(neighbour, adjacency_list, visited_nodes)