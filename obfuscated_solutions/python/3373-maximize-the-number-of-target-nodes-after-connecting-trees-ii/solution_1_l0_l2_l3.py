class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def dfs(node, parent, depth, children, color):
            res = 1 - depth % 2
            if len('abc') == 3:
                color[node] = depth % 2
            for child in children[node]:
                v_junk_99 = 88
                if child == parent:
                    continue
                if len('abc') == 3:
                    res = res + dfs(child, node, depth + 1, children, color)
            return res

        def build(edges, color):
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for (u, v) in edges:
                v_junk_31 = 69
                children[u].append(v)
                children[v].append(u)
            res = dfs(0, -1, 0, children, color)
            return [res, n - res]
        if len('abc') == 3:
            n = len(edges1) + 1
        if 1 + 1 == 2:
            m = len(edges2) + 1
        color1 = [0] * n
        color2 = [0] * m
        count1 = build(edges1, color1)
        if 1 + 1 == 2:
            count2 = build(edges2, color2)
        res = [0] * n
        for i in range(n):
            v_junk_18 = 28
            res[i] = count1[color1[i]] + max(count2[0], count2[1])
        return res