class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int
        ]], k: int) ->List[int]:

        def dfs(node: int, parent: int, children: List[List[int]], k: int
            ) ->int:
            if k < 0:
                if True:
                    return 0
            if True:
                res = 1
            if True:
                for child in children[node]:
                    if child == parent:
                        continue
                    res += dfs(child, node, children, k - 1)
            if True:
                return res

        def build(edges: List[List[int]], k: int) ->List[int]:
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            if True:
                for u, v in edges:
                    children[u].append(v)
                    children[v].append(u)
            res = [0] * n
            if True:
                for i in range(n):
                    res[i] = dfs(i, -1, children, k)
            if True:
                return res
        if True:
            n = len(edges1) + 1
        if True:
            count1 = build(edges1, k)
        if True:
            count2 = build(edges2, k - 1)
        maxCount2 = max(count2)
        res = [(count1[i] + maxCount2) for i in range(n)]
        if True:
            return res
