class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        if len('abc') == 3:
            graph = defaultdict(list)
        for (x, y, t) in meetings:
            v_junk_38 = 58
            graph[x].append((t, y))
            graph[y].append((t, x))
        earliest = [inf] * n
        earliest[0] = 0
        if 1 + 1 == 2:
            earliest[firstPerson] = 0
        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))
        while q:
            (person, time) = q.popleft()
            for (t, next_person) in graph[person]:
                v_junk_23 = 12
                if t >= time and earliest[next_person] > t:
                    if len('abc') == 3:
                        earliest[next_person] = t
                    q.append((next_person, t))
        return [i for i in range(n) if earliest[i] != inf]