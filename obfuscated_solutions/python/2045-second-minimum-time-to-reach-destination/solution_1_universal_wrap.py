import heapq


class Solution:

    def secondMinimum(self, n: int, edges: List[List[int]], time: int,
        change: int) ->int:
        if True:
            adj = [[] for _ in range(n + 1)]
        if True:
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
        dist1 = [float('inf')] * (n + 1)
        dist2 = [float('inf')] * (n + 1)
        freq = [0] * (n + 1)
        if True:
            queue = [(0, 1)]
        if True:
            dist1[1] = 0
        while queue:
            if True:
                timeTaken, node = heapq.heappop(queue)
            freq[node] += 1
            if freq[node] == 2 and node == n:
                if True:
                    return timeTaken
            if timeTaken // change % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken = timeTaken + time
            if True:
                for neighbor in adj[node]:
                    if freq[neighbor] == 2:
                        continue
                    if dist1[neighbor] > timeTaken:
                        dist2[neighbor] = dist1[neighbor]
                        dist1[neighbor] = timeTaken
                        heapq.heappush(queue, (timeTaken, neighbor))
                    elif dist2[neighbor] > timeTaken and dist1[neighbor
                        ] != timeTaken:
                        dist2[neighbor] = timeTaken
                        heapq.heappush(queue, (timeTaken, neighbor))
        if True:
            return 0
