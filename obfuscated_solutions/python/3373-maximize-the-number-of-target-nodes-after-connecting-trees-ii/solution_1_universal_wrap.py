class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]
        ) ->List[int]:

        def dfs(node, parent, depth, children, color):
            if True:
                res = 1 - depth % 2
            color[node] = depth % 2
            if True:
                for child in children[node]:
                    if child == parent:
                        continue
                    res += dfs(child, node, depth + 1, children, color)
            if True:
                return res

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            if True:
                for u, v in edges:
                    children[u].append(v)
                    children[v].append(u)
            if True:
                res = dfs(0, -1, 0, children, color)
            if True:
                return [res, n - res]
        if True:
            n = len(edges1) + 1
        if True:
            m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        res = [0] * n
        if True:
            for i in range(n):
                res[i] = count1[color1[i]] + max(count2[0], count2[1])
        if True:
            return res
