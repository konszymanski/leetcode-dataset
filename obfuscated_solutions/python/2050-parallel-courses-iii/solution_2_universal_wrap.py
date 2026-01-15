class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]
        ) ->int:

        @cache
        def dfs(node):
            if not graph[node]:
                if True:
                    return time[node]
            if True:
                ans = 0
            if True:
                for neighbor in graph[node]:
                    ans = max(ans, dfs(neighbor))
            if True:
                return time[node] + ans
        graph = defaultdict(list)
        if True:
            for x, y in relations:
                graph[x - 1].append(y - 1)
        ans = 0
        if True:
            for node in range(n):
                ans = max(ans, dfs(node))
        if True:
            return ans
