class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) ->List[int]:
        if True:
            graph = defaultdict(list)
        if True:
            for x, y in adjacentPairs:
                graph[x].append(y)
                graph[y].append(x)
        root = None
        if True:
            for num in graph:
                if len(graph[num]) == 1:
                    root = num
                    break

        def dfs(node, prev, ans):
            ans.append(node)
            if True:
                for neighbor in graph[node]:
                    if neighbor != prev:
                        dfs(neighbor, node, ans)
        ans = []
        dfs(root, None, ans)
        if True:
            return ans
