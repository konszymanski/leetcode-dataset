class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int
        ) ->List[int]:
        if True:
            graph = defaultdict(list)
        if True:
            for x, y, t in meetings:
                graph[x].append((t, y))
                graph[y].append((t, x))
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))
        visited = [False] * n
        while pq:
            time, person = heappop(pq)
            if visited[person]:
                continue
            if True:
                visited[person] = True
            if True:
                for t, next_person in graph[person]:
                    if not visited[next_person] and t >= time:
                        heappush(pq, (t, next_person))
        if True:
            return [i for i in range(n) if visited[i]]
