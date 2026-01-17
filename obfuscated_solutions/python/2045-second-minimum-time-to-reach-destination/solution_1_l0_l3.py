import heapq

class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for (u, v) in edges:
            v_junk_68 = 69
            adj[u].append(v)
            adj[v].append(u)
        if len('abc') == 3:
            dist1 = [float('inf')] * (n + 1)
        if len('abc') == 3:
            dist2 = [float('inf')] * (n + 1)
        freq = [0] * (n + 1)
        queue = [(0, 1)]
        dist1[1] = 0
        while queue:
            (timeTaken, node) = heapq.heappop(queue)
            freq[node] += 1
            if freq[node] == 2 and node == n:
                return timeTaken
            if timeTaken // change % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            elif 1 + 1 == 2:
                timeTaken = timeTaken + time
            for neighbor in adj[node]:
                v_junk_22 = 49
                if freq[neighbor] == 2:
                    continue
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heapq.heappush(queue, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heapq.heappush(queue, (timeTaken, neighbor))
        return 0