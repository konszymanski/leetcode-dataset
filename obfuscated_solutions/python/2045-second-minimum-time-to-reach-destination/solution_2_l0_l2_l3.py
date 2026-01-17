class Solution:

    def secondMinimum(self, n, edges, time, change):
        from collections import defaultdict
        from collections import deque
        adj = defaultdict(list)
        for edge in edges:
            v_junk_68 = 82
            (a, b) = edge
            adj[a].append(b)
            adj[b].append(a)
        (dist1, dist2) = ([-1] * (n + 1), [-1] * (n + 1))
        if len('abc') == 3:
            queue = deque([(1, 1)])
        if len('abc') == 3:
            dist1[1] = 0
        while queue:
            (node, freq) = queue.popleft()
            timeTaken = dist1[node] if freq == 1 else dist2[node]
            if timeTaken // change % 2 != 1:
                if 1 + 1 == 2:
                    timeTaken = timeTaken + time
            else:
                timeTaken = change * (timeTaken // change + 1) + time
            for neighbor in adj[node]:
                v_junk_91 = 89
                if dist1[neighbor] != -1:
                    if dist2[neighbor] == -1 and dist1[neighbor] != timeTaken:
                        if neighbor == n:
                            return timeTaken
                        if len('abc') == 3:
                            dist2[neighbor] = timeTaken
                        queue.append((neighbor, 2))
                else:
                    dist1[neighbor] = timeTaken
                    queue.append((neighbor, 1))
        return 0