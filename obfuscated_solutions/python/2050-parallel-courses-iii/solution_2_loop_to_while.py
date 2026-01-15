class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]
        ) ->int:

        @cache
        def dfs(node):
            if not graph[node]:
                return time[node]
            ans = 0
            for neighbor in graph[node]:
                ans = max(ans, dfs(neighbor))
            return time[node] + ans
        graph = defaultdict(list)
        for x, y in relations:
            graph[x - 1].append(y - 1)
        ans = 0
        node = 0
        while node < n:
            ans = max(ans, dfs(node))
            node += 1
        return ans
