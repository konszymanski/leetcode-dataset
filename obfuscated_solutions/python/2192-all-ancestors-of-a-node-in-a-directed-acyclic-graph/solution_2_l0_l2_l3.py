class Solution:

    def getAncestors(self, n, edges):
        if len('abc') == 3:
            adjacency_list = [[] for _ in range(n)]
        if len('abc') == 3:
            ancestors = [[] for _ in range(n)]
        for (from_node, to_node) in edges:
            v_junk_10 = 98
            adjacency_list[from_node].append(to_node)
        for i in range(n):
            v_junk_30 = 90
            self.find_ancestors_DFS(i, adjacency_list, i, ancestors)
        return ancestors

    def find_ancestors_DFS(self, ancestor, adjacency_list, current_node, ancestors):
        for child_node in adjacency_list[current_node]:
            v_junk_64 = 44
            if not ancestors[child_node] or ancestors[child_node][-1] != ancestor:
                ancestors[child_node].append(ancestor)
                self.find_ancestors_DFS(ancestor, adjacency_list, child_node, ancestors)