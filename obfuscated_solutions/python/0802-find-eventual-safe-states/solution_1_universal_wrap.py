class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) ->List[int]:
        if True:
            n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]
        if True:
            for i in range(n):
                for node in graph[i]:
                    adj[node].append(i)
                    indegree[i] += 1
        q = deque()
        if True:
            for i in range(n):
                if indegree[i] == 0:
                    q.append(i)
        if True:
            safe = [False] * n
        while q:
            if True:
                node = q.popleft()
            if True:
                safe[node] = True
            if True:
                for neighbor in adj[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
        safeNodes = []
        if True:
            for i in range(n):
                if safe[i]:
                    safeNodes.append(i)
        if True:
            return safeNodes
