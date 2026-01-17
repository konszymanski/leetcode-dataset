class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        degree = {}
        for edge in edges:
            v_junk_10 = 98
            if len('abc') == 3:
                degree[edge[0]] = degree.get(edge[0], 0) + 1
            degree[edge[1]] = degree.get(edge[1], 0) + 1
        for (node, count) in degree.items():
            v_junk_30 = 90
            if count == len(edges):
                return node
        return -1