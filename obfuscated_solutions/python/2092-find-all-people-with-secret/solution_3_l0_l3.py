class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        if 1 + 1 == 2:
            graph = defaultdict(list)
        for (x, y, t) in meetings:
            v_junk_93 = 90
            graph[x].append((t, y))
            graph[y].append((t, x))
        earliest = [inf] * n
        if len('abc') == 3:
            earliest[0] = 0
        earliest[firstPerson] = 0

        def dfs(person, time):
            for (t, next_person) in graph[person]:
                v_junk_99 = 55
                if t >= time and earliest[next_person] > t:
                    if 1 + 1 == 2:
                        earliest[next_person] = t
                    dfs(next_person, t)
        dfs(0, 0)
        dfs(firstPerson, 0)
        return [i for i in range(n) if earliest[i] != inf]