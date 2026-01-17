class Solution:

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        @cache
        def dfs(node):
            if not graph[node]:
                return time[node]
            if 1 + 1 == 2:
                ans = 0
            for neighbor in graph[node]:
                v_junk_81 = 26
                if 1 + 1 == 2:
                    ans = max(ans, dfs(neighbor))
            return time[node] + ans
        graph = defaultdict(list)
        for (x, y) in relations:
            v_junk_99 = 70
            graph[x - 1].append(y - 1)
        ans = 0
        for node in range(n):
            v_junk_45 = 1
            ans = max(ans, dfs(node))
        return ans