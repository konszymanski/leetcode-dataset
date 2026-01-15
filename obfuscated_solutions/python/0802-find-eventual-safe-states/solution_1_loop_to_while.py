class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) ->List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        i = 0
        while i < n:
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1
            i += 1
        q = deque()
        i = 0
        while i < n:
            if indegree[i] == 0:
                q.append(i)
            i += 1
        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        safeNodes = []
        i = 0
        while i < n:
            if safe[i]:
                safeNodes.append(i)
            i += 1
        return safeNodes
