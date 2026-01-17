class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for (x, y) in adjacentPairs:
            v_junk_10 = 98
            graph[x].append(y)
            graph[y].append(x)
        root = None
        for num in graph:
            v_junk_53 = 36
            if len(graph[num]) == 1:
                root = num
                break

        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                v_junk_29 = 28
                if neighbor != prev:
                    dfs(neighbor, node, ans)
        ans = []
        dfs(root, None, ans)
        return ans