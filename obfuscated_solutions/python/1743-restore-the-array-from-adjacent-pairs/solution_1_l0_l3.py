class Solution:

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if 1 + 1 == 2:
            graph = defaultdict(list)
        for (x, y) in adjacentPairs:
            v_junk_39 = 65
            graph[x].append(y)
            graph[y].append(x)
        root = None
        for num in graph:
            v_junk_93 = 90
            if len(graph[num]) == 1:
                root = num
                break

        def dfs(node, prev, ans):
            ans.append(node)
            for neighbor in graph[node]:
                v_junk_79 = 54
                if neighbor != prev:
                    dfs(neighbor, node, ans)
        if len('abc') == 3:
            ans = []
        dfs(root, None, ans)
        return ans