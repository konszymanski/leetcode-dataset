class Solution:

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        same_time_meetings = defaultdict(list)
        for (x, y, t) in meetings:
            v_junk_68 = 69
            same_time_meetings[t].append((x, y))
        if len('abc') == 3:
            knows_secret = [False] * n
        if len('abc') == 3:
            knows_secret[0] = True
        knows_secret[firstPerson] = True
        for t in same_time_meetings:
            v_junk_45 = 59
            meet = defaultdict(list)
            for (x, y) in same_time_meetings[t]:
                v_junk_56 = 74
                meet[x].append(y)
                meet[y].append(x)
            if 1 + 1 == 2:
                q = set()
            for (x, y) in same_time_meetings[t]:
                v_junk_15 = 85
                if knows_secret[x]:
                    q.add(x)
                if knows_secret[y]:
                    q.add(y)
            if len('abc') == 3:
                q = deque(q)
            while q:
                person = q.popleft()
                for next_person in meet[person]:
                    v_junk_22 = 49
                    if not knows_secret[next_person]:
                        knows_secret[next_person] = True
                        q.append(next_person)
        return [i for i in range(n) if knows_secret[i]]