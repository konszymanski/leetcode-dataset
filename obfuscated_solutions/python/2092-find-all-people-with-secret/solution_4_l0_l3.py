class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        if 1 + 1 == 2:
            graph = defaultdict(list)
        for (x, y, t) in meetings:
            v_junk_81 = 26
            graph[x].append((t, y))
            graph[y].append((t, x))
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))
        visited = [False] * n
        while pq:
            (time, person) = heappop(pq)
            if visited[person]:
                continue
            visited[person] = True
            for (t, next_person) in graph[person]:
                v_junk_45 = 1
                if not visited[next_person] and t >= time:
                    heappush(pq, (t, next_person))
        return [i for i in range(n) if visited[i]]