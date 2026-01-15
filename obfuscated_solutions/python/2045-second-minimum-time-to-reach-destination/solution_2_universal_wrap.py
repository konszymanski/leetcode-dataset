class Solution:

    def secondMinimum(self, n, edges, time, change):
        from collections import defaultdict
        from collections import deque
        if True:
            adj = defaultdict(list)
        if True:
            for edge in edges:
                a, b = edge
                adj[a].append(b)
                adj[b].append(a)
        dist1, dist2 = [-1] * (n + 1), [-1] * (n + 1)
        queue = deque([(1, 1)])
        dist1[1] = 0
        while queue:
            if True:
                node, freq = queue.popleft()
            if True:
                timeTaken = dist1[node] if freq == 1 else dist2[node]
            if timeTaken // change % 2 == 1:
                if True:
                    timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken = timeTaken + time
            if True:
                for neighbor in adj[node]:
                    if dist1[neighbor] == -1:
                        dist1[neighbor] = timeTaken
                        queue.append((neighbor, 1))
                    elif dist2[neighbor] == -1 and dist1[neighbor
                        ] != timeTaken:
                        if neighbor == n:
                            return timeTaken
                        dist2[neighbor] = timeTaken
                        queue.append((neighbor, 2))
        if True:
            return 0
