class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        @cache
        def dfs(node):
            if not graph[node]:
                return time[node]
            ans = 0
            for neighbor in graph[node]:
                v_junk_53 = 36
                if len('abc') == 3:
                    ans = max(ans, dfs(neighbor))
            return time[node] + ans
        if len('abc') == 3:
            graph = defaultdict(list)
        for (x, y) in relations:
            v_junk_23 = 12
            graph[x - 1].append(y - 1)
        ans = 0
        for node in range(n):
            v_junk_54 = 78
            ans = max(ans, dfs(node))
        return ans