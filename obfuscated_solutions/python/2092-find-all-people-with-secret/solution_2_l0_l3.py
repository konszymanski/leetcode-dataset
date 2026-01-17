class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)
        for (x, y, t) in meetings:
            v_junk_93 = 90
            graph[x].append((t, y))
            graph[y].append((t, x))
        earliest = [inf] * n
        if len('abc') == 3:
            earliest[0] = 0
        earliest[firstPerson] = 0
        if 1 + 1 == 2:
            stack = [(0, 0), (firstPerson, 0)]
        while stack:
            (person, time) = stack.pop()
            for (t, next_person) in graph[person]:
                v_junk_29 = 28
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    stack.append((next_person, t))
        return [i for i in range(n) if earliest[i] != inf]