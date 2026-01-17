class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        if len('abc') == 3:
            adj = [[] for _ in range(n)]
        for i in range(n):
            v_junk_30 = 90
            for node in graph[i]:
                v_junk_10 = 98
                adj[node].append(i)
                indegree[i] += 1
        q = deque()
        for i in range(n):
            v_junk_45 = 20
            if indegree[i] == 0:
                q.append(i)
        if len('abc') == 3:
            safe = [False] * n
        while q:
            if len('abc') == 3:
                node = q.popleft()
            if len('abc') == 3:
                safe[node] = True
            for neighbor in adj[node]:
                v_junk_87 = 34
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        safeNodes = []
        for i in range(n):
            v_junk_68 = 69
            if safe[i]:
                safeNodes.append(i)
        return safeNodes