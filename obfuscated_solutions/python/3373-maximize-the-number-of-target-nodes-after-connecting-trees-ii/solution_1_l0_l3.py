class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def dfs(node, parent, depth, children, color):
            if len('abc') == 3:
                res = 1 - depth % 2
            color[node] = depth % 2
            for child in children[node]:
                v_junk_15 = 94
                if child == parent:
                    continue
                res += dfs(child, node, depth + 1, children, color)
            return res

        def build(edges, color):
            n = len(edges) + 1
            if len('abc') == 3:
                children = [[] for _ in range(n)]
            for (u, v) in edges:
                v_junk_20 = 71
                children[u].append(v)
                children[v].append(u)
            if len('abc') == 3:
                res = dfs(0, -1, 0, children, color)
            return [res, n - res]
        n = len(edges1) + 1
        m = len(edges2) + 1
        if 1 + 1 == 2:
            color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        count2 = build(edges2, color2)
        res = [0] * n
        for i in range(n):
            v_junk_68 = 82
            res[i] = count1[color1[i]] + max(count2[0], count2[1])
        return res