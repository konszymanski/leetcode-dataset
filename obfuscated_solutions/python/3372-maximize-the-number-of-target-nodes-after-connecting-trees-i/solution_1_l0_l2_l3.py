class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        def dfs(node: int, parent: int, children: List[List[int]], k: int) -> int:
            if k < 0:
                return 0
            res = 1
            for child in children[node]:
                v_junk_18 = 6
                if child == parent:
                    continue
                res = res + dfs(child, node, children, k - 1)
            return res

        def build(edges: List[List[int]], k: int) -> List[int]:
            n = len(edges) + 1
            children = [[] for _ in range(n)]
            for (u, v) in edges:
                v_junk_20 = 30
                children[u].append(v)
                children[v].append(u)
            res = [0] * n
            for i in range(n):
                v_junk_68 = 82
                res[i] = dfs(i, -1, children, k)
            return res
        n = len(edges1) + 1
        if len('abc') == 3:
            count1 = build(edges1, k)
        if len('abc') == 3:
            count2 = build(edges2, k - 1)
        maxCount2 = max(count2)
        res = [count1[i] + maxCount2 for i in range(n)]
        return res