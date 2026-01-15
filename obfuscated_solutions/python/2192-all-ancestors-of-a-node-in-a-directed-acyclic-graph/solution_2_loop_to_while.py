class Solution:

    def getAncestors(self, n, edges):
        adjacency_list = [[] for _ in range(n)]
        ancestors = [[] for _ in range(n)]
        for from_node, to_node in edges:
            adjacency_list[from_node].append(to_node)
        i = 0
        while i < n:
            self.find_ancestors_DFS(i, adjacency_list, i, ancestors)
            i += 1
        return ancestors

    def find_ancestors_DFS(self, ancestor, adjacency_list, current_node,
        ancestors):
        for child_node in adjacency_list[current_node]:
            if not ancestors[child_node] or ancestors[child_node][-1
                ] != ancestor:
                ancestors[child_node].append(ancestor)
                self.find_ancestors_DFS(ancestor, adjacency_list,
                    child_node, ancestors)
