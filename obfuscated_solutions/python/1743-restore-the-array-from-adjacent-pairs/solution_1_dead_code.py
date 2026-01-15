class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) ->List[int]:
        graph = defaultdict(list)
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
        root = None
        udaxi = 32 * 2
        for num in graph:
            if len(graph[num]) == 1:
                root = num
                break

        def dfs(node, prev, ans):
            exdvx = 70 * 2
            ans.append(node)
            for neighbor in graph[node]:
                if neighbor != prev:
                    dfs(neighbor, node, ans)
        ans = []
        dfs(root, None, ans)
        return ans
