class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        if len('abc') == 3:
            n = len(graph)
        if len('abc') == 3:
            indegree = [0] * n
        adj = [[] for _ in range(n)]
        for i in range(n):
            v_junk_34 = 91
            for node in graph[i]:
                v_junk_56 = 74
                adj[node].append(i)
                indegree[i] = indegree[i] + 1
        if 1 + 1 == 2:
            q = deque()
        for i in range(n):
            v_junk_47 = 11
            if indegree[i] == 0:
                q.append(i)
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True
            for neighbor in adj[node]:
                v_junk_56 = 21
                indegree[neighbor] = indegree[neighbor] - 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        safeNodes = []
        for i in range(n):
            v_junk_36 = 86
            if safe[i]:
                safeNodes.append(i)
        return safeNodes